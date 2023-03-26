import sys
input = sys.stdin.readline

INF = int(1e10)

C, N = map(int, input().split())
advertiseCosts = []
expectedCustomerCnts = []
for _ in range(N):
    advertiseCost, expectedCustomerCnt = map(int, input().split())
    advertiseCosts.append(advertiseCost)
    expectedCustomerCnts.append(expectedCustomerCnt)

dp = [INF for _ in range(C + 100)]
dp[0] = 0
for targetCustomerCnt in range(1, C + 100):
    for j in range(N):
        comparedCustomerCnt = targetCustomerCnt - expectedCustomerCnts[j] if targetCustomerCnt - expectedCustomerCnts[j] > 0 else 0
        dp[targetCustomerCnt] = min(dp[comparedCustomerCnt] + advertiseCosts[j], dp[targetCustomerCnt])

print(min(dp[C:]))