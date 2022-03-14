import math
import collections

def solution(enroll, referral, seller, amount):
    name_num_dict = {name:i for i, name in enumerate(enroll)}
    benefit_per_item = 100
    percent = 0.1
    answer = [0] * len(enroll)
    
    seller_compact_dict = collections.defaultdict(int)
    for idx in range(len(seller)):
        seller_compact_dict[seller[idx]] += amount[idx]
    print(seller_compact_dict)
    
    for idx in range(len(seller)):
        seller_name = seller[idx]
        sell_cnt = amount[idx]
        sell_benefit = (sell_cnt * benefit_per_item)
        parent_benefit = math.floor(sell_benefit * percent)
        # 내 수익
        while True:
            # 내 이익 업데이트
            answer[name_num_dict[seller_name]] += sell_benefit - parent_benefit
            # 부모 이름 찾기
            parent_name = referral[name_num_dict[seller_name]]
            # 나 = 부모로 교체
            seller_name = parent_name
            sell_benefit = parent_benefit
            parent_benefit = math.floor(sell_benefit * percent)
            if parent_name == '-' or sell_benefit == 0:
                break
    
    return answer



# =============================================================== #

import math
import collections

def solution(enroll, referral, seller, amount):
    name_num_dict = {name:i for i, name in enumerate(enroll)}
    benefit_per_item = 100
    percent = 0.1
    answer = [0] * len(enroll)
    
    for idx in range(len(seller)):
        seller_name = seller[idx]
        sell_cnt = amount[idx]
        sell_benefit = (sell_cnt * benefit_per_item)
        parent_benefit = math.floor(sell_benefit * percent)
        answer[name_num_dict[seller_name]] += sell_benefit - parent_benefit
        parent_name = referral[name_num_dict[seller_name]]
        # 내 수익
        while parent_name != '-' and sell_benefit != 0:
            # 나 = 부모로 교체
            seller_name = parent_name
            sell_benefit = parent_benefit
            parent_benefit = math.floor(sell_benefit * percent)
            # 내 이익 업데이트
            answer[name_num_dict[seller_name]] += sell_benefit - parent_benefit
            # 부모 이름 찾기
            parent_name = referral[name_num_dict[seller_name]]
    
    return answer   