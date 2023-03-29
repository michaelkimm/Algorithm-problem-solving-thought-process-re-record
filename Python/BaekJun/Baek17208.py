import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
bugerOrderedCnts = [0]
frenchFriedOrderedCnts = [0]
for _ in range(N):
    x, y = map(int, input().split())
    bugerOrderedCnts.append(x)
    frenchFriedOrderedCnts.append(y)

dp = [[[0]*(K + 1) for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    b = bugerOrderedCnts[i]
    f = frenchFriedOrderedCnts[i]
    for j in range(M + 1):
        for k in range(K + 1):
            dp[i][j][k] = dp[i - 1][j][k]
            if j - b >= 0 and k - f >= 0:
                dp[i][j][k] = max(dp[i - 1][j - b][k - f] + 1, dp[i][j][k])

print(dp[N][M][K])