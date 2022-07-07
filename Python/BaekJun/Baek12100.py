from itertools import product
from collections import deque
import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def getDeque(graph, i, j, q):
  if graph[i][j][0] == 0:
    return False
  if not q or (q[-1][0] != graph[i][j][0]) or (q[-1][1] == True):
    q.append((graph[i][j][0], False))
  else:
    popped = q.pop()
    q.append((popped[0] * 2, True))
  return True

def calGraphWithDeque(graph, i, j, q):
  if not q:
    graph[i][j] = (0, False)
    return False
  value, summed = q.popleft()
  graph[i][j] = (value, False)
  return True

def move(graph, direction):
  N = len(graph)
  # direction이면 맨 direction 부터 direction으로 옮기기
  
  # ex) 우측(동쪽)이면, 맨 우측 부터 우측으로 옮기기

  # 우측
  if direction == 0:
    for i in range(N):
      q = deque([])
      for j in range(N - 1, -1, -1):
        if not getDeque(graph, i, j, q):
          continue
      for j in range(N - 1, -1, -1):
        if not calGraphWithDeque(graph, i, j, q):
          continue
  # 서쪽
  elif direction == 1:
    for i in range(N):
      q = deque([])
      for j in range(0, N):
        if not getDeque(graph, i, j, q):
          continue
      for j in range(0, N):
        if not calGraphWithDeque(graph, i, j, q):
          continue
  # 남쪽
  elif direction == 2:
    for j in range(N):
      q = deque([])
      for i in range(N - 1, -1, -1):
        if not getDeque(graph, i, j, q):
          continue
      for i in range(N - 1, -1, -1):
        if not calGraphWithDeque(graph, i, j, q):
          continue
  elif direction == 3:
    for j in range(N):
      q = deque([])
      for i in range(0, N):
        if not getDeque(graph, i, j, q):
          continue
      for i in range(0, N):
        if not calGraphWithDeque(graph, i, j, q):
          continue

  
def get2DArrayMaxVal(ary):
  result = 0 
  for i in range(len(ary)):
    for j in range(len(ary[0])):
      result = max(result, ary[i][j][0])
  return result
      
  
moveCnt = 5
N = int(input())
inputGraph = [list(map(int, input().split())) for _ in range(N)]

allCases = list(product([idx for idx in range(len(di))], repeat = moveCnt))

answer = 0
for case in allCases:
  tempGraph = [[(inputGraph[i][j], False) for j in range(N)] for i in range(N)]
  for moveDir in case:
    move(tempGraph, moveDir)
  caseMaxVal = get2DArrayMaxVal(tempGraph)
  answer = max(caseMaxVal, answer)
print(answer)


# ================================================== #

import sys
input = sys.stdin.readline

def moveLeft(graph):
  new = []
  N = len(graph)
  for i in range(N):
    prev = -1
    temp = []
    for j in range(N):
      if graph[i][j] == 0:
        continue
      # 이전 번호가 이미 합쳐진 경우
      if prev == -1:
        prev = graph[i][j]
        continue
      # 번호가 같아서 합칠 수 있는 경우
      if prev == graph[i][j]:
        temp.append(prev * 2)
        prev = -1
      # 번호가 달라서 합칠 수 없는 경우
      else:
        temp.append(prev)
        prev = graph[i][j]
    if prev != -1:
      temp.append(prev)
    temp += [0] * (N - len(temp))
    new.append(temp)
  return new

def moveRight(graph):
  temp = [line[::-1] for line in graph]
  return [line[::-1] for line in moveLeft(temp)]

def moveDown(graph):
  temp = list(zip(*graph))
  return list(zip(*moveRight(temp)))

def moveUp(graph):
  temp = list(zip(*graph))
  return list(zip(*moveLeft(temp)))

def dfs(graph, moveCnt):
  if moveCnt == 0:
    return max(map(max, graph))
  v1 = dfs(moveUp(graph), moveCnt - 1)
  v2 = dfs(moveDown(graph), moveCnt - 1)
  v3 = dfs(moveLeft(graph), moveCnt - 1)
  v4 = dfs(moveRight(graph), moveCnt - 1)

  return max(v1, v2, v3, v4)
  
moveCnt = 5
N = int(input())
inputGraph = [list(map(int, input().split())) for _ in range(N)]

print(dfs(inputGraph, moveCnt))