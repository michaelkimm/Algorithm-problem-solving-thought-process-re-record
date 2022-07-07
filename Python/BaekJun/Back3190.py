from collections import deque
import sys
input = sys.stdin.readline

# 북동남서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def changeDirection(curDirection, movement):
  if movement == 'D':
    curDirection = curDirection + 1 if (curDirection + 1) < 4 else 0
  else:
    curDirection = curDirection - 1 if (curDirection - 1) >= 0 else 3
  return curDirection

def move(q, direction, graph, rotateInfo, age):
  head = q[0]
  ni = head[0] + di[direction]
  nj = head[1] + dj[direction]
  if not (0 <= ni < len(graph) and 0 <= nj < len(graph)) or ((ni, nj) in q):
    return False, -1, age
  q.appendleft((ni, nj))
  if graph[ni][nj] == 'a':
    graph[ni][nj] = '-'
  else:
    q.pop()
  age += 1
  if rotateInfo[age] != '-':
    direction = changeDirection(direction, rotateInfo[age])
  return True, direction, age


# 입력
N = int(input())
K = int(input())
graph = [['-' for _ in range(N)] for _ in range(N)]
for _ in range(K):
  appleRow, appleCol = map(int, input().split())
  graph[appleRow - 1][appleCol - 1] = 'a'

L = int(input())
rotateInfo = ['-' for _ in range(10001)]
for _ in range(L):
  X, C = input().split()
  rotateInfo[int(X)] = C

# 초기화
direction = 1
age = 0
q= deque([(0, 0)])

# 움직이기 실행
result = True
while result:
  result, direction, age = move(q, direction, graph, rotateInfo, age)

print(age + 1)