from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    # 각 메뉴 콤비 카운트
    menu_combi = defaultdict(int)
    for order in orders:
        tmp_order = sorted([ch for ch in order])    # (X,Y), (Y,X)는 (X,Y)로 통일 by sort
        for cnt in range(2, len(order) + 1):
            tmp_combi = list(combinations(tmp_order, cnt))
            for combi in tmp_combi:
                menu_combi[combi] += 1
                
    result = []
    # n개로 구성된 코스가 최대 나온 횟수
    combi_candi_val = defaultdict(int)
    # n개로 구성된 코스 리스트
    combi_candidates = defaultdict(list)
    for key in menu_combi.keys():
        if menu_combi[key] >= 2 and len(key) in course:
            if combi_candi_val[len(key)] == menu_combi[key]:
                combi_candidates[len(key)].append(key)
            elif combi_candi_val[len(key)] < menu_combi[key]:
                combi_candi_val[len(key)] = menu_combi[key]
                combi_candidates[len(key)] = [key]
                
    # char to string
    for len_course in course:
        for char_tuple in combi_candidates[len_course]:
            result.append(''.join(char_tuple))
    
    result.sort()
    return result