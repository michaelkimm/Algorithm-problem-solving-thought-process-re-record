import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)

for num in range(2, N + 1):
  # 1 빼기
  dp[num] = dp[num - 1] + 1
  
  # 5 나누기
  #if num % 5 == 0:
  #  dp[num] = min(dp[num // 5] + 1, dp[num])
  # 3 나누기
  if num % 3 == 0:
    dp[num] = min(dp[num // 3] + 1, dp[num])
  # 2 나누기
  if num % 2 == 0:
    dp[num] = min(dp[num // 2] + 1, dp[num])

print(dp[N])