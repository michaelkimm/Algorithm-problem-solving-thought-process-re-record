import sys
input = sys.stdin.readline

# 입력
n = int(input())
dp = list(map(int, input().split()))

for i in range(1, n):
  # 이전에 합했던게 음수면 넘어간다.
  # dp[i] = dp[i - 1] + dp[i]
  if dp[i - 1] <= 0:
    continue
  dp[i] = dp[i - 1] + dp[i]

print(max(dp))