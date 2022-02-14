import sys
input = sys.stdin.readline

N, M = map(int, input().split())
papers = [int(input()) for _ in range(N)]
dp = [M + 1] * (M + 1)
dp[0] = 0

for target in range(1, M + 1):
  for paper in papers:
    if target - paper >= 0 and dp[target - paper] != (M + 1):
      dp[target] = min(dp[target - paper] + 1, dp[target])

if dp[M] == M + 1:
  print(-1)
else:
  print(dp[M])
print(dp)