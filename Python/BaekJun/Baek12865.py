import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N):
    w = items[i][0]
    v = items[i][1]
    for j in range(1, K + 1):

        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(max(list(max(v) for v in dp)))