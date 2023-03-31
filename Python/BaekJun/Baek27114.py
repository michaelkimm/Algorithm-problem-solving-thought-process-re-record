import sys
input = sys.stdin.readline

INF = int(1e10)

L, R, B, K = map(int, input().split())

dp = [INF for _ in range(K + 1)]

LR = (2, L + R)
LLB = (3, L + L + B)
LLLL = (4, 4 * L)
RRRR = (4, 4 * R)
RRB = (3, R + R + B)
BB = (2, 2 * B)

movements = [LR, LLB, LLLL, RRRR, RRB, BB]

dp[0] = 0
for i in range(1, K + 1):
    for moveCnt, cost in movements:
        if i - cost >= 0:
            dp[i] = min(dp[i], dp[i - cost] + moveCnt)

print(dp[K] if dp[K] != INF else -1)