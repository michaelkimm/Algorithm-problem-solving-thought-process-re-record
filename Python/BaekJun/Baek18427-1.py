import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
blocks = [[]]
for _ in range(N):
    blocks.append([0] + list(map(int, input().split())))

dp = [[0 for _ in range(H + 1)] for _ in range(N + 1)]
dp[0][0] = 1
for idx in range(1, N + 1):
    for height in range(H + 1):
        tmp = 0
        for block in blocks[idx]:
            if height - block < 0:
                continue
            tmp += dp[idx - 1][height - block]
        dp[idx][height] = tmp

print(dp[N][H] % 10007)