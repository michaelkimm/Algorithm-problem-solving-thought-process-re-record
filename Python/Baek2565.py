import sys
input = sys.stdin.readline

N = int(input())
threadList = list(list(map(int, input().split())) for _ in range(N))
dp = [1] * N

threadList.sort(key = lambda x: (x[0], x[1]))

for i in range(N):
  for j in range(i):
    if threadList[j][1] < threadList[i][1]:
      dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))