from bisect import bisect_right

def check_ridable(bus_depart_times, timetable, idx, m):
    right = 0
    for bus_depart_time in bus_depart_times:
        seat_left = m
        while right <= len(timetable) - 1 and timetable[right] <= bus_depart_time and seat_left >= 1:
            seat_left -= 1
            right += 1
        #print("s:", seat_left, "idx:", idx)
        # 가능 판정
        if right > idx:
            return True
    return False        

def calculate_time(t, passed):
    h, m = t.split(":")
    tmp_h, tmp_m = divmod((int(m) + int(passed)), 60)
    return str(tmp_h + int(h)).zfill(2) + ":" + str(tmp_m).zfill(2)

def solution(n, t, m, timetable):
    initial_depart_time = "09:00"
    answer = ''
    
    # 버스 출발 시간
    bus_depart_times = [initial_depart_time]
    for i in range(1, n):
        bus_depart_times.append(calculate_time(bus_depart_times[-1], t))
    # 크루들 정렬
    timetable.sort()
    # 크루 바로 앞에 슬 경우
    timetable_minus_one = [calculate_time(time, -1) for time in timetable]
    # 콘이 서있을 시간 경우의 수
    time_set_list = sorted(set(timetable + bus_depart_times + timetable_minus_one))
    ridable_times = []
    for idx in range(len(time_set_list)):
        time = time_set_list[idx]
        tmp_times = [t for t in timetable]
        # 특정 시간의 맨 오른쪽에서 콘은 서있는다
        insert_needed_loc = bisect_right(timetable, time)
        tmp_times.insert(insert_needed_loc, time)
        # 해당 경우의 수에서 콘이 버스를 탈 수 있나?
        if check_ridable(bus_depart_times, tmp_times, insert_needed_loc, m):
            ridable_times.append(time)
        else:
            break
        
    return ridable_times[-1]