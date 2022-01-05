import sys
input = sys.stdin.readline

N = int(input())
numberList = [list(map(int, input().split())) for _ in range(N)]

indexList = [N - 1 for _ in range(N)]

result = 0
for _ in range(N):
  maxIdx = 0
  maxVal = -10000000000
  for i in range(N):
    if len(numberList) > 0:
      if numberList[indexList[i]][i] > maxVal:
        maxVal = numberList[indexList[i]][i]
        maxIdx = i
  
  result = maxVal
  indexList[maxIdx] -= 1
  
print(result)