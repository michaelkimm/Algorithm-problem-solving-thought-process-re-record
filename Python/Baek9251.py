import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

dp = [[0 for _ in range(len(str1))] for _ in range(len(str2))]

for i in range(len(str2)):
  for j in range(len(str1)):
    # i - 1 vs 만약 두 문자 같으면 i - 1, j - 1 vs j - 1값
    up = dp[i - 1][j] if i - 1 >= 0 else 0
    upLeft = 0
    if str2[i] == str1[j]:
      upLeft = dp[i - 1][j - 1] + 1 if j - 1 >= 0 and i - 1 >= 0 else 1
      
    left = dp[i][j - 1] if j - 1 >= 0 else 0

    dp[i][j] = max(up, upLeft, left)

print(max(max(dp)))