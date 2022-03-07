from itertools import combinations
from collections import defaultdict

def solution(str1, str2):
    str1_dict = defaultdict(int)
    str2_dict = defaultdict(int)
    for idx in range(len(str1) - 1):
        if str1[idx].isalpha() and str1[idx + 1].isalpha():
            str1_dict[str1[idx].lower() + str1[idx + 1].lower()] += 1
    for idx in range(len(str2) - 1):
        if str2[idx].isalpha() and str2[idx + 1].isalpha():
            str2_dict[str2[idx].lower() + str2[idx + 1].lower()] += 1
    
    intersection_cnt = 0
    union_cnt = 0
    for key1 in str1_dict.keys():
        if key1 in str2_dict.keys():
            intersection_cnt += min(str1_dict[key1], str2_dict[key1])
            union_cnt += max(str1_dict[key1], str2_dict[key1])
        else:
            union_cnt += str1_dict[key1]
    
    for key2 in str2_dict.keys():
        if key2 not in str1_dict.keys():
            union_cnt += str2_dict[key2]
    
    
    result = 0
    if intersection_cnt == 0 and union_cnt == 0:
        result = 65536
    elif intersection_cnt == 0 and union_cnt != 0:
        result = 0
    else:
        result = int((intersection_cnt / union_cnt) * 65536)
    
    return result