import sys
input = sys.stdin.readline

N, x = map(int, input().split())
pipeLengths = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    L, C = map(int, input().split())
    for j in range(1, C + 1):
        pipeLengths[i].append(L * j)

dp = [[0 for _ in range(x + 1)] for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(x + 1):
        dp[i][j] = dp[i - 1][j]
        for pipeLength in pipeLengths[i]:
            if j - pipeLength >= 0:
                dp[i][j] += dp[i - 1][j - pipeLength]

print(dp[N][x])