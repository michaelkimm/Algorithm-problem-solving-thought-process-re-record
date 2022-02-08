import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append((1,v))
  graph[v].append((1,u))

distance[1] = 0
heap = [(0, 1)]

while heap:
  dist, node = heapq.heappop(heap)
  if distance[node] < dist:
    continue

  for d, n in graph[node]:
    newCost = dist + d
    if newCost < distance[n]:
      distance[n] = newCost
      heapq.heappush(heap, (newCost, n))

maxCost = 0
cnt = 0
pose = 0
for node in range(1, N + 1):
  if distance[node] >= INF:
    continue
  if maxCost < distance[node]:
    cnt = 1
    pose = node
    maxCost = distance[node]
  elif maxCost == distance[node]:
    cnt += 1
    
print(pose, maxCost, cnt)