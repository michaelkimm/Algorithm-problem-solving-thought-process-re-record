import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

dpStr = [["" for _ in range(len(str1))] for _ in range(len(str2))]

for i in range(len(str2)):
  for j in range(len(str1)):
    # i - 1 vs 만약 두 문자 같으면 i - 1, j - 1 vs j - 1값
    up = dpStr[i - 1][j] if i - 1 >= 0 else ""

    upLeft = ""
    if str2[i] == str1[j]:
      upLeft = dpStr[i - 1][j - 1] + str2[i] if j - 1 >= 0 and i - 1 >= 0 else str2[i]
      
    left = dpStr[i][j - 1] if j - 1 >= 0 else ""

    result = max(len(up), len(upLeft), len(left))
    if result == len(up):
      dpStr[i][j] = up
    elif result == len(upLeft):
      dpStr[i][j] = upLeft
    else:
      dpStr[i][j] = left

result = ""
for line in dpStr:
  tmpResult = max(line, key=len)
  if len(tmpResult) > len(result):
    result = tmpResult 

print(len(result))
print(result)