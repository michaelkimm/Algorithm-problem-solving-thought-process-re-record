import sys
input = sys.stdin.readline

N = int(input())

# dp 초기화
dp = [[0 for _ in range(10)] for _ in range(N + 1)]
for i in range(10):
  dp[1][i] = 1
dp[1][0] = 0

for n in range(2, N + 1):
  for i in range(10):
    if (n - 1 >= 0 and i - 1 >= 0):
      dp[n][i] += dp[n - 1][i - 1]
    if (n - 1 >= 0 and i + 1 <= 9):
      dp[n][i] += dp[n - 1][i + 1]

print(sum(dp[N]) % 1000000000)