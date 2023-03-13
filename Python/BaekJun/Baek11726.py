import sys
input = sys.stdin.readline

def solution(n):
    if n == 1:
        return 1
    
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

n = int(input())

result = solution(n)
print(result % 10007)