import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

intmax = 999999999

dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

for i in range(len(str1)):
  for j in range(len(str2)):
    # 예외 처리
    if i == 0 and j == 0:
      dp[i][j] = 0 if str1[i] == str2[j] else 1
      continue

    up = dp[i - 1][j] + 1 if i - 1 >= 0 else intmax

    if str1[i] == str2[j]:
      upLeft = dp[i - 1][j - 1] if j - 1 >= 0 and i - 1 >= 0 else j + i
    else:
      upLeft = dp[i - 1][j - 1] + 1 if j - 1 >= 0 and i - 1 >= 0 else intmax
      
    left = dp[i][j - 1] + 1 if j - 1 >= 0 else intmax

    dp[i][j] = min(up, upLeft, left)
    
print(dp[len(str1) - 1][len(str2) - 1])