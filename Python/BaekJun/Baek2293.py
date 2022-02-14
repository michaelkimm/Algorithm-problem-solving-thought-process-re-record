import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# dp 초기화
dp = [0] * (10001)

for coin in coins:
  if coin > k:
    continue
  dp[coin] += 1
  for cost in range(coin + 1, k + 1):
    dp[cost] += dp[cost - coin]

print(dp[k])