import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

# 입력
V, E = map(int, input().split())
start = int(input().strip())

visited = [False] * (V + 1)
shortestDist = [INF] * (V + 1)
dist = [[] for _ in range(V + 1)]

# 간선 정보 입력 받기
for _ in range(E):
  u, v, d = map(int, input().split())
  dist[u].append((v, d))

# 다익스트라
heap = []   # (노드까지 거리 최소, 노드)
shortestDist[start] = 0
heapq.heappush(heap, (0, start))

while heap:
  curMinDist, node = heapq.heappop(heap)
  
  if visited[node]:
    continue

  visited[node] = True

  # 최단거리 초기화
  for v, d in dist[node]:
    newCost = shortestDist[node] + d
    if newCost < shortestDist[v]:
      shortestDist[v] = newCost
      heapq.heappush(heap, (newCost, v)) 
  
for idx in range(1, len(shortestDist)):
  if shortestDist[idx] == INF:
    print("INF")
  else:
    print(shortestDist[idx])