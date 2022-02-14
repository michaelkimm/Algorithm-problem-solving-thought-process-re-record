import sys
input = sys.stdin.readline

N = int(input())
feedBoxList = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
  if i == 0 or i == 1:
    dp[i] = max(feedBoxList[:i + 1])
    continue
  
  dp[i] = max(dp[i - 2] + feedBoxList[i], dp[i - 1])
  
print(dp[N - 1])