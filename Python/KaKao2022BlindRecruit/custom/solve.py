import argparse
import re

from http_json import http_method

ABILITY_MIN = 1000
ABILITY_MAX = 100000
ABILITY_AVG = 40000
ABILITY_STD = 20000

scenario = {
    1 : {'user_cnt':30, 'request_freq':1},
    2 : {'user_cnt':900, 'request_freq':45}
    }

get_method = lambda sub_url : http_method("GET", args.base_url, sub_url, token=TOKEN)
post_method = lambda sub_url, data : http_method("POST", args.base_url, sub_url, data=data, token=TOKEN)
put_method = lambda sub_url, data : http_method("PUT", args.base_url, sub_url, data=data, token=TOKEN)

def start_api(base_url, init_token, problem):
    response = http_method("POST", base_url, "/start", data={'problem': problem}, token=init_token, init=True)
    if type(response) is dict:
        return response.get('auth_key', '')
    return ''

def game_result_api():
    resp = get_method("/game_result").get("game_result", [])
    # print("game_result_resp:", resp)
    return [[d['win'], d['lose'], d['taken']]for d in resp]

def waiting_line_api(now_time):
    # GET /waiting_line
    # Authorization: {auth_key}
    # Content-Type: application/json
    resp = get_method("/waiting_line").get("waiting_line", [])

    # id	Integer	매칭을 기다리고 있는 유저의 ID
    # from	Integer	매칭 대기를 시작한 시각(턴)
    return [[d['id'], now_time - d['from']] for d in resp]

def match_api(data):
    # PUT /match
    # Authorization: {auth_key}
    # Content-Type: application/json
    response = put_method("/match", {'pairs': data})
    status = response.get("status", "")
    time = response.get("time", 0)
    # print("status, time:", status, time)

def score_api():
    return get_method("/score")

def change_grade_api(user_ability):
    # PUT /change_grade
    # Authorization: {auth_key}
    # Content-Type: application/json

    abilitySorted = sorted(user_ability.items(), key=lambda x:x[1], reverse=True)
    commands = [{'id':abilitySorted[idx], 'grade':idx + 1} for idx in range(len(abilitySorted))]
    return put_method("/change_grade", {"commands": commands})

def api_change_grade(skills, num_users):
    # skills에서 value 기준으로 정렬해 id만 저장
    grades = [k for k, _ in sorted(skills.items(), key=lambda item: item[1], reverse=True)]
    # {id: index}로 저장
    commands = [{'id': id, 'grade': grades.index(id)} for id in range(1, num_users+1)]
    return put_method("/change_grade", {"commands": commands})

def get_predict_taken(user1_ability, user2_ability):
    ret = 40 - int(abs(user1_ability - user2_ability) / 99000 * 35)
    if ret < 3:
        ret = 3
    elif ret > 40:
        ret = 40
    return ret

def update_participant(user_participate_cnt, win_id, lose_id):
    user_participate_cnt[win_id] += 1
    user_participate_cnt[lose_id] += 1

def update_ability(user_ability, win_id, lose_id, weight):
    # winner 실력 높이고
    user_ability[win_id] = min(ABILITY_MAX, user_ability[win_id] + weight)
    # loser 실력 낮추고
    user_ability[lose_id] = max(ABILITY_MIN, user_ability[lose_id] - weight)

def solve(args):
    problem_number = 1
    global TOKEN
    TOKEN = start_api(args.base_url, args.init_token, args.problem)
    user_cnt = scenario[problem_number]['user_cnt']
    user_ability = {(id + 1):ABILITY_AVG for id in range(user_cnt)}
    user_participate_cnt = {(id + 1):0 for id in range(user_cnt)}
    for now_time in range(595 + 1):
        # 게임 결과 받아오기
        game_results = game_result_api()
        # 대기열 받아오기
        waiting_line = waiting_line_api(now_time)

        # 능력 재배열
        for win_id, lose_id, real_taken in game_results:

            update_participant(user_participate_cnt, win_id, lose_id)

            predict_taken = get_predict_taken(win_id, lose_id)
            taken_diff = predict_taken - real_taken
            
            ability_diff = abs(predict_taken - real_taken) // 2 * args.weight
            
            udate_weight = (40 - real_taken) * 10

            update_ability(user_ability, win_id, lose_id, 5 * (taken_diff))


        # 전략적으로 매칭 / 나중z
        # 555턴 부터는 WaitingLine API는 빈 배열만을 반환하며 Match API는 어떤 유저도 매칭시키지 못한다.
        # (id, ability, 기다린 시간)
        waiting_line.sort(key=lambda x:(user_ability[x[0]], x[1]), reverse=True)
        
        idx = 0
        match_list = []
        min_match_diff = 2001
        while idx + 1 < len(waiting_line):
            id1, waited_time1 = waiting_line[idx]
            id2, waited_time2 = waiting_line[idx + 1]
            
            # match_list.append([id1, id2])
            # idx += 2
            
            # 일정 실력차 이하만 매칭시키기
            ability_diff = abs(user_ability[id1] - user_ability[id2])
            # 아직x : 오래 기다리면 가중치 더 넣어주기 
            if ability_diff <= min_match_diff:
                match_list.append([id1, id2])
                idx += 2
            else:
                idx += 1
        if now_time != 595:
            match_api(match_list)

    # 등급 업데이트
    api_change_grade(user_ability, user_cnt)

    # 턴 끝
    match_api([])

    return score_api()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", type=int, default=1)
    parser.add_argument("--base-url", type=str, required=True)
    parser.add_argument("--init-token", type=str, required=True)
    parser.add_argument("--weight", type=int, default=1)
    args = parser.parse_args()
    print(solve(args))