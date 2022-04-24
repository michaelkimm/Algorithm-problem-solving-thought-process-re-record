from itertools import combinations_with_replacement

def get_score_diff(my_record, enemy_record):
    # my[2,1,1,1,0,0,0,0,0,0,0]
    # en[1,2,4,0,0,0,0,0,0,0,0]
    my_result = 0
    enemy_result = 0
    for idx in range(len(my_record)):
        score = 10 - idx
        if my_record[idx] == 0 and enemy_record[idx] == 0:
            continue
        if my_record[idx] > enemy_record[idx]:
            my_result += score
        else:
            enemy_result += score
    return my_result - enemy_result if my_result > enemy_result else -1

def solution(n, info):
    max_score = 0
    max_score_records = []
    # 0~10까지 중복해서 n개 뽑기 (중복 조합)
    shot_cases = list(combinations_with_replacement(range(11), n))
    # 모든 라이언 슛 경우 고려
    for shot_case in shot_cases:
        shot_record = [0] * 11
        for shot in shot_case:
            shot_record[shot] += 1
            
        # 라이언이 이길 수 있는 경우인지 판단
        score_compare_result = get_score_diff(shot_record, info)
        if score_compare_result != -1:
            # 이길 수 있는 경우
            if score_compare_result == max_score:
                max_score_records.append(shot_record)
            elif score_compare_result > max_score:
                max_score = score_compare_result
                max_score_records = [shot_record]
    max_score_records.sort(key=lambda x: (-x[10], -x[9], -x[8], -x[7], -x[6], -x[5], -x[4], -x[3], -x[2], -x[1], -x[0]))
    return max_score_records[0] if max_score_records else [-1]