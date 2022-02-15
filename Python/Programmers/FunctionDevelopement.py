import math

def solution(progresses, speeds):
    answer = []
    max_time_cost = 0
    tmp_cnt = 0
    numExist = False
    for progress, speed in zip(progresses, speeds):
        time_cost = math.ceil((100 - progress) / speed)
        if tmp_cnt == 0:
            max_time_cost = time_cost
            tmp_cnt = 1
        elif time_cost > max_time_cost:
            max_time_cost = time_cost
            answer.append(tmp_cnt)
            tmp_cnt = 1
        else:
            tmp_cnt += 1
    
    answer.append(tmp_cnt)
    return answer