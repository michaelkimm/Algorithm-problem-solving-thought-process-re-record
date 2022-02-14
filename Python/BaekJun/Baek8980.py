from collections import deque
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
boxInfoList = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[1])

queue = deque(boxInfoList)
boxAvailableList = [C] * (N + 1)
result = 0

while queue:
  boxInfo = queue.popleft()
  # 1. 탑승 마을 <= x < 내림 마을 사이에서 적재 가능한 화물 수 최솟 값 얻기
  minLoadableCnt = min(boxAvailableList[boxInfo[0] : boxInfo[1]])

  # 2. 탑승 마을 <= x < 내림 마을 사이 -> 적재 가능 화물 값 -= 1번의 최솟 값
  load = minLoadableCnt if boxInfo[2] > minLoadableCnt else boxInfo[2]
  result += load

  for i in range(boxInfo[0], boxInfo[1]):
    boxAvailableList[i] -= load

print(result)