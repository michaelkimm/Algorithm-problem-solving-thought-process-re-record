def solution(n):
    answer = 0
    bf = 1
    bbf = 0
    cur = 1
    for _ in range(n):
        cur = bf + bbf
        bbf, bf = bf, cur
    return cur % 1000000007


# ================================= #

def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    if n == 1:
        return 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    answer = dp[n]
    return answer