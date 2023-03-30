import sys
input = sys.stdin.readline

INF = int(1e10)

def getCombinedPipeCapacity(c1, c2):
    return c1 if c1 < c2 else c2

D, P = map(int, input().split())
lengths = [0]
capacities = [0]
for _ in range(P):
    l, c = map(int, input().split())
    lengths.append(l)
    capacities.append(c)

dp = [INF] + [0]*D

for i in range(1, P + 1):
    dpMax = dp.copy()
    for j in range(1, D + 1):
        if j - lengths[i] >= 0 and dpMax[j - lengths[i]] != 0:
            dp[j] = max(getCombinedPipeCapacity(dpMax[j - lengths[i]], capacities[i]), dpMax[j])

print(dp[D])