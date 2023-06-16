import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memorys = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [0 for _ in range(10001)]
dp[0] = 0

for i in range(N):
    mem = memorys[i]
    cost = costs[i]
    for j in range(10000, -1, -1):
        dp[j] = max(dp[j - cost] + mem, dp[j]) if j >= cost else dp[j]

answer = 0
for i in range(10001):
    if dp[i] >= M:
        answer = i
        break
print(answer)