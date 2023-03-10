import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N + 1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for sz in range(2, N + 1):
    for end in range(10):
        if end == 0:
            dp[sz][end] = dp[sz - 1][end + 1]
        elif end == 9:
            dp[sz][end] = dp[sz - 1][end - 1]
        else:
            dp[sz][end] = dp[sz - 1][end - 1] + dp[sz - 1][end + 1]

print(sum(dp[N]) % 1000000000)