# =================================================================== #
# 플로이드 워셜 풀이
# =================================================================== #

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

T = int(input().strip())
resultList = []

def GetMyIndex(i, j, n):
  return N * i + (j + 1)

for _ in range(T):
  # 입력
  N = int(input().strip())
  inputGraph2d = []
  
  graph2d = [[INF] * (N * N + 1) for _ in range(N * N + 1)]
  
  for _ in range(N):
    row = list(map(int, input().split()))
    inputGraph2d.append(row)

  # i, j 상하좌우에서 i, j로 올려면 필요한 비용
  for i in range(N):
    for j in range(N):
      # 상
      if i - 1 >= 0:
        graph2d[GetMyIndex(i - 1, j, N)][GetMyIndex(i, j, N)] = inputGraph2d[i][j]
      # 하
      if i + 1 <= N - 1:
        graph2d[GetMyIndex(i + 1, j, N)][GetMyIndex(i, j, N)] = inputGraph2d[i][j]
      # 좌
      if j - 1 >= 0:
        graph2d[GetMyIndex(i, j - 1, N)][GetMyIndex(i, j, N)] = inputGraph2d[i][j]
      # 우
      if j + 1 <= N - 1:
        graph2d[GetMyIndex(i, j + 1, N)][GetMyIndex(i, j, N)] = inputGraph2d[i][j]

  startCost = inputGraph2d[0][0]
  for i in range(N * N + 1):
    graph2d[i][i] = 0

  for mid in range(N * N + 1):
    for i in range(N * N + 1):
      for j in range(N * N + 1):
        graph2d[i][j] = min(graph2d[i][j], graph2d[i][mid] + graph2d[mid][j])

  for i in range(N * N + 1):
      for j in range(N * N + 1):
        graph2d[i][j] += startCost

  # for line in graph2d:
  #   print(line)
  resultList.append(graph2d[1][N * N])

for result in resultList:
  print(result)

# =================================================================== #
# 다익스트라 풀이
# =================================================================== #

  import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

T = int(input().strip())
resultList = []

def GetMyIndex(i, j, n):
  return N * i + (j + 1)

for _ in range(T):
  # 입력
  N = int(input().strip())
  inputGraph2d = []
  
  for _ in range(N):
    row = list(map(int, input().split()))
    inputGraph2d.append(row)

  graph = [[] for _ in range(N * N + 1)]
  # 방향 입력 받기
  for i in range(N):
    for j in range(N):
      # 상하좌우에서 i, j로 들어오는 간선
      # 상
      if i - 1 >= 0:
        graph[GetMyIndex(i - 1, j, N)].append((inputGraph2d[i][j], GetMyIndex(i, j, N)))
      # 하
      if i + 1 <= N - 1:
        graph[GetMyIndex(i + 1, j, N)].append((inputGraph2d[i][j], GetMyIndex(i, j, N)))
      # 좌
      if j - 1 >= 0:
        graph[GetMyIndex(i, j - 1, N)].append((inputGraph2d[i][j], GetMyIndex(i, j, N)))
      # 우
      if j + 1 <= N - 1:
        graph[GetMyIndex(i, j + 1, N)].append((inputGraph2d[i][j], GetMyIndex(i, j, N)))
  # 다익스트라
  shortDist = [INF] * (N * N + 1)

  heap = []
  shortDist[1] = inputGraph2d[0][0]
  heapq.heappush(heap, (shortDist[1], 1))

  while heap:
    dist, node = heapq.heappop(heap)
    if dist > shortDist[node]:
      continue
    
    for d, v in graph[node]:
      newCost = min(shortDist[v], shortDist[node] + d)
      if newCost < shortDist[v]:
        shortDist[v] = newCost
        heapq.heappush(heap, (newCost, v))

  resultList.append(shortDist[N * N])

for result in resultList:
  print(result)