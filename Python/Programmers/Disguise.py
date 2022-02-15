from collections import Counter

def solution(clothes):
    answer = 1
    
    # 의상 갯수 세기
    cnt = Counter([key for name, key in clothes])
    
    for key in cnt.keys():
        answer *= (cnt[key] + 1)
    
    # 의상 조합에서 총 경우의 수 도출
    return answer - 1

    # ===================================================== #

from collections import Counter
from functools import reduce

def solution(clothes):
    answer = 1
    
    cnt = Counter([key for name, key in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1)
    
    return answer - 1