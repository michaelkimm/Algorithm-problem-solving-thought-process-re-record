import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

N, M, C = map(int, input().split())

shortDist = [INF] * (N + 1)
distance = [[]for _ in range(N + 1)]

for _ in range(M):
  X, Y, Z = map(int, input().split())
  distance[X].append((Y, Z))

heap = []
shortDist[C] = 0
heapq.heappush(heap, (0, C))

while heap:
  dist, node = heapq.heappop(heap)

  if shortDist[node] < dist:
    continue
  
  for v, d in distance[node]:
    newCost = shortDist[node] + d
    if newCost < shortDist[v]:
      shortDist[v] = newCost
      heapq.heappush(heap, (shortDist[v], v))

cnt = 0
maxTime = 0
for node in range(1, N + 1):
  if shortDist[node] < INF and shortDist[node] != 0:
    cnt += 1
    maxTime = max(maxTime, shortDist[node])

print(shortDist)

print(cnt, maxTime)