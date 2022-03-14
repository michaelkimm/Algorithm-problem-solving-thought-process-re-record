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
    
    timetable.sort()
    min_arridable_time = [calculate_time(min(timetable[0], bus_depart_times[0]), -1)]
    timetable_minus_one = [calculate_time(time, -1) for time in timetable]
    time_set_list = sorted(set(timetable + bus_depart_times + min_arridable_time + timetable_minus_one))
    #print(time_set_list)
    ridable_times = []
    for idx in range(len(time_set_list)):
        time = time_set_list[idx]
        tmp_times = [t for t in timetable]
        insert_needed_loc = bisect_right(timetable, time)
        tmp_times.insert(insert_needed_loc, time)
        if check_ridable(bus_depart_times, tmp_times, insert_needed_loc, m):
            ridable_times.append(time)
        else:
            break
        
    return ridable_times[-1] if ridable_times else -1