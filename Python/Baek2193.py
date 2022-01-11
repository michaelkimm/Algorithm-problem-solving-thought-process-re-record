import sys
input = sys.stdin.readline

N = int(input())

# dp 초기화
dp = [[0 for _ in range(2)] for _ in range(N + 1)]
dp[1][1] = 1

for i in range(2, N + 1):
  dp[i][1] = dp[i - 1][0]
  dp[i][0] = dp[i - 1][0] + dp[i - 1][1]

print(sum(dp[N]))