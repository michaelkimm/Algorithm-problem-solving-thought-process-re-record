import sys
input = sys.stdin.readline

# 입력
n = int(input())
ary = list(map(int, input().split()))
dp = [0] * n


for i in range(n):
  for j in range(i):
    if ary[j] > ary[i]:
      dp[i] = max(dp[i], dp[j])
  dp[i] += 1

print(n - max(dp))