import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = sorted([list(map(int, input().split())) for _ in range(N)])

dp = [0 for _ in range(K + 1)]

for weight, value in items:
    for i in range(K, weight - 1, -1):
        dp[i] = max(dp[i - weight] + value, dp[i])

print(dp[K])
