def solution(n, weak, dist):
    dist.sort(reverse=True)
    total_fixable_cases = [set()]
    count = 0
    for d in dist:
        count += 1
        # 1. 시간당 d만큼 가는 인부가 w 위치에서 시작할 때 고칠 수 있는 취약점 구하기
        fixable_cases = []
        for w in weak:
            fixable_sites = set([site % n for site in range(w, w + d + 1) if site % n in weak])
            fixable_cases.append(fixable_sites)
            
        # 2. 앞에 인부가 고칠 수 있는 곳과 합쳐서 판단 후 저장
        cand = set()
        for pre_union_case in total_fixable_cases:
            for fixable_sites in fixable_cases:
                new = set(pre_union_case).union(fixable_sites)
                if len(new) == len(weak):
                    return count
                cand.add(tuple(new))
        total_fixable_cases = cand
    return -1