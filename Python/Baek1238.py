import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v, d = map(int, input().split())
  graph[u].append((d, v))

shortDist = [INF] * (N + 1)

def dijkstra(start, end):
  global shortDist

  # 최소 거리 초기화
  for i in range(len(shortDist)):
    shortDist[i] = INF

  heap = [(0, start)]
  shortDist[start] = 0

  while heap:
    dist, node = heapq.heappop(heap)
    if shortDist[node] < dist:
      continue

    for d, v in graph[node]:
      newCost = dist + d
      if newCost < shortDist[v]:
        shortDist[v] = newCost
        heapq.heappush(heap, (newCost, v))

  return shortDist[end]

maxCost = 0
for node in range(1, N + 1):
  cost = dijkstra(node, X) + dijkstra(X, node)
  # print("node:", node, " cost:", cost)
  if cost > maxCost:
    maxCost = cost

print(maxCost)