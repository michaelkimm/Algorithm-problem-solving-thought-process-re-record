from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    # 각 메뉴 콤비 카운트
    menu_combi = defaultdict(int)
    for order in orders:
        for course_size in course:
            # (X,Y), (Y,X)는 (X,Y)로 통일 by sort
            tmp_combi = list(combinations(sorted(order), course_size))
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

# ====================================================== #
from collections import Counter
from itertools import combinations

def solution(orders, course):
    result = []
    for course_size in course:
        combi_list = []
        for order in orders:
            # (X,Y), (Y,X)는 (X,Y)로 통일 by sort
            combi_list += combinations(sorted(order), course_size)
            
        most_common_list = Counter(combi_list).most_common()
        # 1번 이상 나타남 and 최대 빈도 수와 같은 경우 추가
        result += [k for k, v in most_common_list if v > 1 and v == most_common_list[0][1]]
    
    return sorted([''.join(k) for k in result])