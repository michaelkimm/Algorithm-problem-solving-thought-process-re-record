import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
graphReversed = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v = map(int, input().split())
  # u가 v 보다 키가 작다
  graph[u].append(v)
  graphReversed[v].append(u)

shortDistance = [INF] * (N + 1)

def dijkstra(start, graph_):
  global shortDistance

  heap = [(0, start)]
  shortDistance[start] = 0

  while heap:
    dist, node = heapq.heappop(heap)
    if shortDistance[node] < dist:
      continue

    for v in graph_[node]:
      newCost = dist + 1
      if newCost < shortDistance[v]:
        shortDistance[v] = newCost
        heapq.heappush(heap, (newCost, v))

  cnt = 0
  for dist in shortDistance:
    if dist < INF:
      cnt += 1
  # 최단거리 초기화
  for i in range(len(shortDistance)):
    shortDistance[i] = INF

  # 자기 자신 제외
  return cnt - 1

cnt = 0
for node in range(1, N + 1):
  if dijkstra(node, graph) + dijkstra(node, graphReversed) == N - 1:
    cnt +=1

print(cnt)