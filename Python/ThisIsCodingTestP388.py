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