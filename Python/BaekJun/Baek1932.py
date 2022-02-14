# 풀이 1
import sys
input = sys.stdin.readline

N = int(input())
triangle = []
for _ in range(N):
  temp = list(map(int, input().split()))
  for num in temp:
    triangle.append(num)

dp = [0] * len(triangle)
floor = []
for num in range(1, N + 1):
  for _ in range(num):
    floor.append(num)

dp[0] = triangle[0]

for i in range(1, len(triangle)):
  upLeft = -1 if i - floor[i] < 0 or floor[i] - floor[i - floor[i]] != 1 else dp[i - floor[i]]
  upRight = -1 if floor[i] - floor[i - (floor[i] - 1)] != 1 else dp[i - (floor[i] - 1)]
  dp[i] = max(upLeft, upRight) + triangle[i]

print(max(dp))



# 풀이 2
import sys
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
  for j in range(len(dp[i])):
    upLeft = 0 if i - 1 < 0 or j - 1 < 0 else dp[i - 1][j - 1]
    upRight = 0 if i - 1 < 0 or j >= len(dp[i - 1]) else dp[i - 1][j]
    dp[i][j] = max(upLeft, upRight) + dp[i][j]

print(max(max(dp)))


# 풀이 3
import sys
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
  for j in range(i + 1):
    # 왼쪽 위
    if j == 0:
      upLeft = 0
    else:
      upLeft = dp[i - 1][j - 1]

    # 바로 위
    if i == j:
      upRight = 0
    else:
      upRight = dp[i - 1][j]

    dp[i][j] = max(upLeft, upRight) + dp[i][j]

print(max(max(dp)))



# 풀이 4
import sys
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
  for j in range(i + 1):
    upLeft = 0 if j == 0 else dp[i - 1][j - 1]
    upRight = 0 if i == j else dp[i - 1][j]
    dp[i][j] = max(upLeft, upRight) + dp[i][j]

print(max(max(dp)))