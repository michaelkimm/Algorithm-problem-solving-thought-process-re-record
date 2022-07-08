from collections import deque
import sys
input = sys.stdin.readline

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

def getReverseDir(direction):
  if direction == 1:
    return 2
  elif direction == 2:
    return 1
  elif direction == 3:
    return 4
  else:
    return 3

def move(dice, top, direction):
  # 방향
  hIdx = 0
  vIdx = 0
  if direction in [1, 2]:
    vIdx = 1
    hIdx = 0 if direction == 1 else 2
  else:
    hIdx = 1
    vIdx = 0 if direction == 4 else 2
  temp = top
  top = dice[vIdx][hIdx]
  dice[vIdx][hIdx] = dice[1][1]
  dice[1][1] = dice[2 - vIdx][2 - hIdx]
  dice[2 - vIdx][2 - hIdx] = temp
  return dice, top

# input
N, M, ci, cj, K = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))
commands = deque(list(map(int, input().split())))

# 초기화
top = 0
dice = [[0, 0, 0] for _ in range(3)]

while commands:
  cmd = commands.popleft()
  dice, top = move(dice, top, cmd)
  ni = ci + di[cmd]
  nj = cj + dj[cmd]
  if not (0 <= ni < N and 0 <= nj < M):
    dice, top = move(dice, top, getReverseDir(cmd))
    continue
  ci, cj = ni, nj
  if graph[ci][cj] == 0:
    graph[ci][cj] = dice[1][1]
  else:
    dice[1][1] = graph[ci][cj]
    graph[ci][cj] = 0
  print(top)
    