import itertools
def solution(relation):
    # 8C1 ~ 8C8 = 250
    # 각 키당 20번씩 검색
    key_check_list = []
    for i in range(1, len(relation[0]) + 1):
        for tuple_k in itertools.combinations(range(len(relation[0])), i):
            key_check_list.append(set(k for k in tuple_k))
            
    candidate_keys = []
    answer = 0
    for key in key_check_list:
        available = True
        # 최소성 확인
        for ck in candidate_keys:
            if key.intersection(ck) == ck:
                available = False
                break
        if not available:
            continue
            
        # 유일성 확인
        tmp_set = set()
        for data in relation:
            data_piece = tuple(data[k] for k in key)
            tmp_set.add(data_piece)
        if len(tmp_set) == len(relation):
            candidate_keys.append(key)
            answer += 1
        
    return answer




# ============================================== #

import itertools

def solution(relation):
    # 8C1 ~ 8C8 = 250
    # 각 키당 20번씩 검색
    key_check_list = []
    for i in range(1, len(relation[0]) + 1):
        key_check_list.extend(set(k for k in tuple_k) for tuple_k in itertools.combinations(range(len(relation[0])), i))
            
    candidate_keys = []
    answer = 0
    for key in key_check_list:
        available = True
        # 최소성 확인
        for ck in candidate_keys:
            if ck.issubset(key):
                available = False
                break
        if not available:
            continue
            
        # 유일성 확인
        tmp_set = set()
        for data in relation:
            data_piece = tuple(data[k] for k in key)
            tmp_set.add(data_piece)
        if len(tmp_set) == len(relation):
            candidate_keys.append(key)
            answer += 1
        
    return answer