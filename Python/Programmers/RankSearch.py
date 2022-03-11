import itertools
import collections
import bisect

def solution(infos, querys):
    condition_cnt = 4
    info_dict = collections.defaultdict(list)
    binarys = list(itertools.product((True, False), repeat=condition_cnt))
    
    # 하나의 info가 16개 키에 속하게됨
    # 하나의 info로 16개 키 생성 알고리즘?
    for info in infos:
        info_list = info.split()
        for binary in binarys:
            key = ''.join([info_list[i] if binary[i] else '-' for i in range(condition_cnt)])
            info_dict[key].append(int(info_list[4]))
            
    for key in info_dict.keys():
        info_dict[key].sort()
        
    answer = []        
    for query in querys:
        lan, _, job, _, career, _, sf, score  = query.split()
        key = lan + job + career + sf
        cnt = len(info_dict[key]) - bisect.bisect_left(info_dict[key], int(score))
        answer.append(cnt)
    return answer


# ============================================= #


import itertools
import collections
import bisect

def solution(info, query):
    answer = []
    info_map = collections.defaultdict(list)
    
    for inf in info:
        inf_list = inf.split()
        for l in [inf_list[0], '-']:
            for j in [inf_list[1], '-']:
                for c in [inf_list[2], '-']:
                    for sf in [inf_list[3], '-']:
                        key = l + j + c + sf
                        info_map[key].append(int(inf_list[4]))
                        
    for key in info_map.keys():
        info_map[key].sort()
        
    for q in query:
        lan, _, job, _, career, _, sf, score = q.split()
        key = lan + job + career + sf
        answer.append(len(info_map[key]) - bisect.bisect_left(info_map[key], int(score)))
    return answer