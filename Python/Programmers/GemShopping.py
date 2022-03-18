from collections import defaultdict
def solution(gems):
    gems_cnt_dict = defaultdict(int)
    gems_cnt = len(gems)
    gems_type_cnt = len(set(gems))
    start, end = 0, 0
    min_cnt = int(1e10)
    result = [0, 0]
    
    for start, gem in enumerate(gems):
        while len(gems_cnt_dict) < gems_type_cnt and end <= gems_cnt - 1:
            gems_cnt_dict[gems[end]] += 1
            end += 1
        if len(gems_cnt_dict) == gems_type_cnt:
            if min_cnt > end - start:
                min_cnt = end - start
                result = [start + 1, end]
        gems_cnt_dict[gem] -= 1
        if gems_cnt_dict[gem] <= 0:
            del gems_cnt_dict[gem]
    return result