import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())
cmpFwdList = [[] for _ in range(N + 1)]
cmpBwdList = [[] for _ in range(N + 1)]
for _ in range(M):
  A, B = map(int, input().split())
  # A < B
  cmpFwdList[A].append((1, B))
  cmpBwdList[B].append((1, A))

shortDist = [INF] * (N + 1)

def dijkstraFwd(start, shortDist):
  heap = []
  heapq.heappush(heap, (0, start))
  shortDist[start] = 0

  while heap:
    dist, node = heapq.heappop(heap)
    if dist > shortDist[node]:
      continue

    for d, n in cmpFwdList[node]:
      newCost = min(shortDist[n], shortDist[node] + d)
      if newCost < shortDist[n]:
        shortDist[n] = newCost
        heapq.heappush(heap, (newCost, n))

  # 갈 수 있는 노드 갯수 반환
  cnt = 0
  for d in shortDist:
    if d != INF:
      cnt += 1
  
  # shortDist 초기화
  for i in range(len(shortDist)):
    shortDist[i] = INF

  # 자기 자신 제외
  return cnt - 1

def dijkstraBwd(start):
  heap = []
  heapq.heappush(heap, (0, start))
  shortDist[start] = 0

  while heap:
    dist, node = heapq.heappop(heap)
    if dist > shortDist[node]:
      continue

    for d, n in cmpBwdList[node]:
      newCost = min(shortDist[n], shortDist[node] + d)
      if newCost < shortDist[n]:
        shortDist[n] = newCost
        heapq.heappush(heap, (newCost, n))

  # 갈 수 있는 노드 갯수 반환
  cnt = 0
  for d in shortDist:
    if d != INF:
      cnt += 1
  
  # shortDist 초기화
  for i in range(len(shortDist)):
    shortDist[i] = INF

  # 자기 자신 제외
  return cnt - 1

result = 0
for start in range(1, N + 1):
  if dijkstraFwd(start) + dijkstraBwd(start) == N - 1:
    result += 1

print(result)