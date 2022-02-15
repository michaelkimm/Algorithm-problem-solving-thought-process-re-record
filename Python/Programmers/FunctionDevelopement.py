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


# ================================================================== #
import math

def solution(progresses, speeds):
    answer = []
    tmp_cnt = 1
    time_left = list(map(lambda x: math.ceil((100 - progresses[x]) / speeds[x]), range(len(progresses))))
    
    for i in range(len(progresses)):
        try:
            if time_left[i] < time_left[i + 1]:
                answer.append(tmp_cnt)
                tmp_cnt = 1
            else:
                time_left[i + 1] = time_left[i]
                tmp_cnt += 1
        except IndexError:
            answer.append(tmp_cnt)
    
    return answer