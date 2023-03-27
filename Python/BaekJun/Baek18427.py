import sys
input = sys.stdin.readline

INF = int(1e10)

N, K = map(int, input().split())
caffeines = list(map(int, input().split()))
dp = [[INF for _ in range(100001)] for _ in range(N)]

for i in range(N):
    dp[i][0] = 0

dp[0][caffeines[0]] = 1

for i in range(1, N):
    for j in range(1, K + 1):
        dp[i][j] = min(dp[i - 1][j - caffeines[i]] + 1, dp[i - 1][j])

possibleAnswer = min(list(zip(*dp))[K])
answer = possibleAnswer if (possibleAnswer < INF) else -1
print(answer)