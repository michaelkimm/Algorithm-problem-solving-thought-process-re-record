import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

def solution(dp, N, K):
    
    for i in range(K + 1):
        dp[i][0] = 1

    for i in range(K + 1):
        for j in range(1, N + 1):
            for coin in range(N + 1):
                if i - 1 >= 0 and j - coin >= 0:
                    dp[i][j] += dp[i - 1][j - coin]

    return dp[K][N]

print(solution(dp, N, K) % 1_000_000_000)