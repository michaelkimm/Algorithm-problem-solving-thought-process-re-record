import sys
input = sys.stdin.readline

INF = int(1e10)

N, M = map(int, input().split())
memorys = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
costSum = sum(costs)

dp = [[0 for _ in range(costSum + 1)] for _ in range(N + 1)] # i번째까지 앱을 사용하여 j 비용을 사용했을 때얻을 수 있는 최대 메모리 바이트 수

for i in range(1, N + 1):
    for j in range(costSum + 1):
        dp[i][j] = dp[i - 1][j]
        if j - costs[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - costs[i]] + memorys[i])

answer = -1
for j in range(costSum + 1):
    if dp[N][j] >= M:
        answer = j
        break
print(answer)
