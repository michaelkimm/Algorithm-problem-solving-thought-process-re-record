import sys
input = sys.stdin.readline

INF = int(1e9)

# 입력
n = int(input().strip())
m = int(input().strip())

# 간선 정보
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
  u, v, d = map(int, input().split())
  if d > graph[u][v]:
    continue
  graph[u][v] = d

# 자기 자신으로 가는 것 초기화
for i in range(1, n + 1):
  graph[i][i] = 0

# 플로이드 워셜
for mid in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      graph[i][j] = min(graph[i][j], graph[i][mid] + graph[mid][j])


for i in range(1, n + 1):
  for j in range(1, n + 1):
    if (graph[i][j] == INF):
      print(0, end=' ')
    else:
      print(graph[i][j], end=' ')
  print("")