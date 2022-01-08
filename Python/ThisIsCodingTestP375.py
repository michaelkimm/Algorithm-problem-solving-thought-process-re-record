import sys
input = sys.stdin.readline

def array1Dto2D(ary, n, m):
  result = []
  for i in range(n):
    tmp = []
    for j in range(m):
      tmp.append(ary[i * m + j])
    result.append(tmp)
  return result

def FindMaxGold(mine):
  # 가로
  for j in range(len(mine[0])):
    # 세로
    for i in range(len(mine)):
      temp = mine[i][j]
      # 뒤, 뒤위, 뒤아래 중에 최대로 설정
      if j - 1 >= 0:
        temp = mine[i][j - 1] + mine[i][j]
      if j - 1 >= 0 and i - 1 >= 0:
        temp = max(mine[i - 1][j - 1] + mine[i][j], temp)
      if j - 1 >= 0 and i + 1 <= len(mine) - 1:
        temp = max(mine[i + 1][j - 1] + mine[i][j], temp)
      mine[i][j] = temp
  
  return max(map(max, mine))

T = int(input())
result = []

for _ in range(T):
  n, m = map(int, input().split())
  temp = list(map(int, input().split()))
  goldMine = array1Dto2D(temp, n, m)
  result.append(FindMaxGold(goldMine))

print(result)






# 깔끔 버전
import sys
input = sys.stdin.readline

def FindMaxGold(mine):
  # 가로
  for j in range(1, len(mine[0])):
    # 세로
    for i in range(len(mine)):
      # 왼
      left = mine[i][j - 1] + mine[i][j]
      # 왼위
      if i == 0:
        leftUp = 0
      else:
        leftUp = mine[i - 1][j - 1] + mine[i][j]

      # 왼 아래
      if i == n - 1:
        leftDown = 0
      else:
        leftDown = mine[i + 1][j - 1] + mine[i][j]
      mine[i][j] = max(left, leftUp, leftDown)
  
  return max(map(max, mine))

T = int(input())
result = []


for _ in range(T):
  # 금광 정보 입력
  n, m = map(int, input().split())
  temp = list(map(int, input().split()))

  # dp 초기화
  dp = []
  index = 0
  for i in range(n):
    dp.append(temp[index:index + m])
    index += m

  # 계산 진행
  result.append(FindMaxGold(dp))

print(result)

