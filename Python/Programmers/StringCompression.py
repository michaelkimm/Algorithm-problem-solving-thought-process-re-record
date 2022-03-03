def solution(s):
    iter_unit = 1
    left_idx, cmp_l_idx = 0, 0
    min_len = int(1e10)
    if len(s) <= 1:
        return 1
    
    while iter_unit < len(s):
        tmp_len = len(s)
        tmp_iter_cnt = 1
        left_idx, cmp_l_idx = 0, 0
        while left_idx < len(s) - 1:
            # 런타임 에러 조심 s 길이 1
            cmp_l_idx += iter_unit
            if s[left_idx:left_idx + iter_unit] == s[cmp_l_idx:cmp_l_idx + iter_unit]:
                tmp_iter_cnt += 1
                # cmp를 한칸 더 옮김
                continue
            else:
                # left를 업데이트
                left_idx = cmp_l_idx
                if tmp_iter_cnt > 1:
                    tmp_len -= (tmp_iter_cnt - 1) * (iter_unit) 
                    tmp_len += len(str(tmp_iter_cnt)) 
                    tmp_iter_cnt = 1
        iter_unit += 1
        min_len = min(tmp_len, min_len)
    answer = min_len
    return answer