import sys
input = sys.stdin.readline

# 북동남서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def getLeftDirection(direction):
  return direction - 1 if (direction - 1) >= 0 else 3

def getLeftPose(i, j, direction):
  direction = getLeftDirection(direction)
  ni = i + di[direction]
  nj = j + dj[direction]
  return ni, nj

def getBackPose(i, j, direction):
  direction = getLeftDirection(getLeftDirection(direction))
  ni = i + di[direction]
  nj = j + dj[direction]
  return ni, nj
  
# 입력
N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))

cleanedCnt = 0
ci, cj = r, c
direction = d
rotateCnt = 0

cnt = 0
while True:
  # 1번
  if graph[ci][cj] == 0:
    cleanedCnt += 1
    graph[ci][cj] = 2
  li, lj = getLeftPose(ci, cj, direction)
  # 2-a
  if graph[li][lj] == 0:
    direction = getLeftDirection(direction)
    ci, cj = li, lj
    rotateCnt = 0
  else:
    # 2-a
    direction = getLeftDirection(direction)
    rotateCnt += 1
    # 2-b
    if rotateCnt >= 4:
      bi, bj = getBackPose(ci, cj, direction)
      if graph[bi][bj] == 1:
        break
      else:
        ci, cj = bi, bj
        rotateCnt = 0
        
print(cleanedCnt)