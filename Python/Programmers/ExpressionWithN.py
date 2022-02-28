import math
def get_continuous_num(num, cnt):
    result = 0
    for i in range(0, cnt):
        result += int(math.pow(10, i) * num)
    return result

def solution(N, number):
    max_miv_val = 9
    dp = [set() for _ in range(max_miv_val)]
    n_used_cnt = 0
    for k in range(1, max_miv_val):
        
        # dp[k] = set(dp[i] + dp[k - i] for i in range(1, k))
        # 붙이기
        
        dp[k].add(get_continuous_num(N, k))
        # 더하기
        for i in range(1, k):
            for i_val in dp[i]:
                for k_i_val in dp[k - i]:
                    dp[k].add(i_val + k_i_val)
        # 뺄셈
        for i in range(1, k):
            for i_val in dp[i]:
                for k_i_val in dp[k - i]:
                    dp[k].add(i_val - k_i_val)
                    dp[k].add(k_i_val - i_val)
        # 곱셈
        for i in range(1, k):
            for i_val in dp[i]:
                for k_i_val in dp[k - i]:
                    dp[k].add(i_val * k_i_val)
        # 나눗셈
        for i in range(1, k):
            for i_val in dp[i]:
                for k_i_val in dp[k - i]:
                    if k_i_val != 0:
                        dp[k].add(i_val // k_i_val)
                    if i_val != 0:
                        dp[k].add(k_i_val // i_val)
        # print(dp[k])
        
        if number in dp[k]:
            n_used_cnt = k
            break
    if n_used_cnt == 0:
        n_used_cnt = -1
    answer = n_used_cnt
    return answer