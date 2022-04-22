from collections import defaultdict

def solution(id_list, report, k):
    user_id_idx = {}
    for idx, ID in enumerate(id_list):
        user_id_idx[ID] = idx
    
    reported_dict = defaultdict(set)
    for r in report:
        reporter, reported = r.split()
        reported_dict[reported].add(reporter)

    answer = [0] * len(id_list)
    for reported in reported_dict.keys():
        if len(reported_dict[reported]) >= k:
            for reporter in reported_dict[reported]:
                answer[user_id_idx[reporter]] += 1
    return answer