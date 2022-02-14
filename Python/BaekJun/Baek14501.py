import sys
input = sys.stdin.readline

N = int(input())
ary = list(list(map(int, input().split())) for _ in range(N))
p = []
d = []
for dist, price in ary:
  p.append(price)
  d.append(dist)

dp = [0] * N

for i in range(N - 1, -1, -1):
  # 오늘 일 선택x
  todayNo = dp[i + 1] if i + 1 < N else 0

  # 오늘 일 선택o
  if i + d[i] < N:
    todayYes = p[i] + dp[i + d[i]]
  elif i + d[i] == N:
    todayYes = p[i]
  else:
    todayYes = 0

  dp[i] = max(todayNo, todayYes)

print(max(dp))