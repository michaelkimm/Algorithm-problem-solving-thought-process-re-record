import sys
input = sys.stdin.readline

INF = int(1e10)

N, T = map(int, input().split())
times = [0]
points = [0]
for _ in range(N):
    time, point = map(int, input().split())
    times.append(time)
    points.append(point)

dp = [[0 for _ in range(T + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, T + 1):
        if j >= times[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - times[i]] + points[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][T])