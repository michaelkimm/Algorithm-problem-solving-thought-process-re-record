import argparse

from http_json import http_method

scenario = {
    1 : {'hotel_size':(3, 20), 'max_date':200, 'req_max_room_cnt':10, 'max_stay_date':20},
    2 : {'hotel_size':(10, 200), 'max_date':1000, 'req_max_room_cnt':50, 'max_stay_date':100}
    }

get_method = lambda sub_url : http_method("GET", args.base_url, sub_url, token=TOKEN)
post_method = lambda sub_url, data : http_method("POST", args.base_url, sub_url, data=data, token=TOKEN)
put_method = lambda sub_url, data : http_method("PUT", args.base_url, sub_url, data=data, token=TOKEN)

def start_api(base_url, init_token, problem):
    response = http_method("POST", base_url, "/start", data={'problem': problem}, token=init_token, init=True)
    if type(response) is dict:
        return response.get('auth_key', '')
    return ''

def new_request_api():
    resp = get_method("/new_requests").get("reservations_info", [])

    # [id, amount, check_in_date, check_out_date]
    return [[d['id'], d['amount'], d['check_in_date'], d['check_out_date']] for d in resp]

def score_api():
    return get_method("/score")

def simulate_api(room_assign):
    # input = [[id, room_number], [id, room_number]]
    cmd = [{"id":id, "room_number":room_number} for id, room_number in room_assign]
    # output = [{ "id": 412424, "room_number": "1002"}, { "id": 707981, "room_number": "3020"}, ...]
    return put_method("/simulate", {"room_assign": cmd})

def reply_api(replies):
    # input = [[id, reply], [id, reply]]
    cmd = [{"id":id, "reply":reply} for id, reply in replies]
    # output = [{ "id": 412424, "reply": "accepted"}, { "id": 707981, "reply": "refused"}, ...]
    return put_method("/reply", {"replies": cmd})

def get_room_number_in_format(i, j):
    return str(i) + str(j).zfill(3)

def get_available_room_number(room, amount, virtual=False, now=1, check_in_date=1):
    for i in range(1, len(room)):
        for j in range(1, len(room[0])):
            if j + amount >= len(room[0]):
                break
            room_state = set(room[i][j:j+amount])
            if len(room_state) == 1 and (0 in room_state):
                # 사용할 수 있는 객실이면
                for dj in range(amount):
                    if not virtual:
                        room[i][j + dj] = amount
                    else:
                        room[i][j + dj] = (check_in_date - now) + amount
                return get_room_number_in_format(i, j)
    return ''

def update_room_state(room):
    for i in range(1, len(room)):
        for j in range(1, len(room[0])):
            room[i][j] = room[i][j] - 1 if room[i][j] - 1 >= 0 else 0

def accept_all_request(reservation_request_infos, reserved_infos):
    replies = []
    for id, amount, check_in_date, check_out_date in reservation_request_infos:
        replies.append([id, 'accepted'])
        reserved_infos[check_in_date].append((id, amount, check_out_date))
    return replies

def accept_request_with_room_cnt_greedy(reservation_request_infos, reserved_infos):
    replies = []
    reservation_request_infos.sort(key=lambda x:(x[1], x[3]))
    for id, amount, check_in_date, check_out_date in reservation_request_infos:
        replies.append([id, 'accepted'])
        reserved_infos[check_in_date].append((id, amount, check_out_date))
    return replies

def accept_request_with_room_cnt_greedy_n(reservation_request_infos, reserved_infos, n):
    replies = []
    reservation_request_infos.sort(key=lambda x:(x[1], x[3]))
    for id, amount, check_in_date, check_out_date in reservation_request_infos:
        if amount <= n:
            replies.append([id, 'refused'])
            continue
        replies.append([id, 'accepted'])
        reserved_infos[check_in_date].append((id, amount, check_out_date))
    return replies

def accept_request_with_room_cnt_duration_greedy(reservation_request_infos, reserved_infos, room_cnt_n, duration):
    replies = []
    reservation_request_infos.sort(key=lambda x:(x[1], x[3]))
    for id, amount, check_in_date, check_out_date in reservation_request_infos:
        if amount <= room_cnt_n or (check_out_date - check_in_date) >= duration:
            replies.append([id, 'refused'])
            continue
        replies.append([id, 'accepted'])
        reserved_infos[check_in_date].append((id, amount, check_out_date))
    return replies

def reply_n_days_later(reservation_request_infos, reserved_infos, room_cnt_n, duration, n_days_stored):
    # 방 크고 빨리 끝나고
    # 기존 n_days 저장 건 보다 [방이 크고] and 새것.[시작 시간] < 기존것.[체크아웃 시간] 기존 것 빼고 지금 것 넣기
    replies = []
    reservation_request_infos.sort(key=lambda x:(x[1], x[3]))
    for id, amount, check_in_date, check_out_date in reservation_request_infos:
        
        
        
        if amount <= room_cnt_n or (check_out_date - check_in_date) >= duration:
            continue
        replies.append([id, 'accepted'])
        reserved_infos[check_in_date].append((id, amount, check_out_date))
    return replies

def accept_request_with_room_cnt_duration_greedy_and_virtually_give_room(reservation_request_infos, reserved_infos, room, room_cnt_n, duration, now, virtual_room_number):
    replies = []
    # reservation_request_infos.sort(key=lambda x:(-x[1], x[3]))
    reservation_request_infos.sort(key=lambda x:(x[3], -x[1]))
    for id, amount, check_in_date, check_out_date in reservation_request_infos:
        if amount <= room_cnt_n or (check_out_date - check_in_date) >= duration:
            replies.append([id, 'refused'])
            continue
        replies.append([id, 'accepted'])
        reserved_infos[check_in_date].append((id, amount, check_out_date))
        # 가상 방 주기
        room_number = get_available_room_number(room, amount, virtual=True, now=now, check_in_date=check_in_date)
        virtual_room_number[id] = room_number
    return replies

def accept_request_with_room_cnt_duration_greedy_and_virtually_give_room_safe(reservation_request_infos, reserved_infos, room, room_cnt_n, duration, now, virtual_room_number):
    replies = []
    # reservation_request_infos.sort(key=lambda x:(-x[1], x[3]))
    reservation_request_infos.sort(key=lambda x:(x[3], -x[1]))
    for id, amount, check_in_date, check_out_date in reservation_request_infos:
        
        # 가상 방 주기
        room_number = get_available_room_number(room, amount, virtual=True, now=now, check_in_date=check_in_date)
        if room_number != '':
            virtual_room_number[id] = room_number
            replies.append([id, 'accepted'])
            reserved_infos[check_in_date].append((id, amount, check_out_date))
        else:
            replies.append([id, 'refused'])
            continue

    return replies

def solve(args):
    global TOKEN
    TOKEN = start_api(args.base_url, args.init_token, args.problem)
    day = 1
    # 3층 10개 호수 -> 4층 10개 호수로 설정 (0행, 0열 사용x)
    room = [[0 for _ in range(scenario[args.problem]['hotel_size'][1] + 1)] for _ in range(scenario[args.problem]['hotel_size'][0] + 1)]
    # reserved_info
    reserved_infos = [[] for _ in range(scenario[args.problem]['max_date'] + 1)]

    n_days_stored = []
    virtual_room_number = {}

    result = []

    reply_in_deadline = [[] for _ in range(scenario[args.problem]['max_date'] + 1)]

    while day < scenario[args.problem]['max_date']:
        reservation_request_infos = new_request_api()

        # 정답은 무조건 데드라인에 대답
        # 데드라인 = min(예약 요청이 들어온 날짜 + 14 , 체크인 날짜 - 1)
        for id, amount, check_in_date, check_out_date in reservation_request_infos:
            deadline = min(day + 14, check_in_date - 1)
            reply_in_deadline[deadline].append((id, amount, check_in_date, check_out_date))

        # 데드라인 중에서 replies 생성
        room_cnt_n = 2 if args.problem == 1 else 10
        duration = 10 if args.problem == 1 else 40
        replies = accept_request_with_room_cnt_duration_greedy_and_virtually_give_room_safe(
            reservation_request_infos=reply_in_deadline[day],
            reserved_infos=reserved_infos,
            room=room,
            room_cnt_n=room_cnt_n,
            duration=duration,
            now=day,
            virtual_room_number=virtual_room_number
            )

        # 수락 혹은 거절 
        resp = reply_api(replies)

        # 가상방 부여한 것에서 오늘 진짜로 체크인할 사람
        room_assign = []
        for id, amount, check_out_date in sorted(reserved_infos[day], key=lambda x:(-x[2], x[1]), reverse=True):
            room_number = virtual_room_number.get(id, '')
            if room_number == '':
                continue
            room_assign.append([id, room_number])
        
        # 입소
        resp = simulate_api(room_assign)
        day = resp['day']
        result.append(resp['fail_count'])

        update_room_state(room)
        
    print(result)
    simulate_api([])

    return score_api()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", type=int, default=1)
    parser.add_argument("--base-url", type=str, required=True)
    parser.add_argument("--init-token", type=str, required=True)
    parser.add_argument("--weight", type=int, default=1)
    args = parser.parse_args()
    print(solve(args))