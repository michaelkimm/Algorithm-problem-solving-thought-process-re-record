def get_overlapped_info(prev_start, prev_end, prev_cnt, new_start, new_end):
    if new_start > prev_end:
        return new_start, new_end, 1
    elif new_start >= prev_start and prev_end <= new_end:
        return new_start, prev_end, prev_cnt + 1
    else: # new_start >= prev_start and new_end <= prev_end:
        return new_start, new_end, prev_cnt + 1
def solution(routes):
    routes.sort()
    cur_idx = 1
    answer = 0
    # 시작, 끝, 겹친 횟수
    overlapped_info = [routes[cur_idx][0], routes[cur_idx][1], 1]
    while cur_idx <= len(routes) - 1:
        new_start, new_end, new_cnt = get_overlapped_info(overlapped_info[0], overlapped_info[1], overlapped_info[2], routes[cur_idx][0], routes[cur_idx][1])
        
        # 새로 삽입됨
        if overlapped_info[2] >= new_cnt:
            answer += 1
        overlapped_info = [new_start, new_end, new_cnt]
        cur_idx += 1
    # overlapped_info 남아있는 것 추출
    answer += 1
    return answer

# ======================================== #

def solution(routes):
    camera_candidate = -30001
    routes.sort(key=lambda x:x[1])
    answer = 0
    for route in routes:
        if camera_candidate < route[0]:
            answer += 1
            camera_candidate = route[1]
    return answer