from collections import deque
import sys
input = sys.stdin.readline

def topology_sort(graph, entry_list, N):
  q = deque()
  for node in range(1, N + 1):
    if entry_list[node] == 0:
      q.append(node)

  rank = []
  impossible = False
  uncertain = False
  while q:
    if len(q) >= 2:
      uncertain = True
      break

    node = q.popleft()
    rank.append(node)
    
    for v in range(1, N + 1):
      if graph[node][v]:
        entry_list[v] -= 1
        if entry_list[v] == 0:
          q.append(v)

  for node in range(1, N + 1):
    if entry_list[node] != 0 and len(q) == 0:
      impossible = True
      break

  if uncertain:
    return ("?", False)
  elif impossible:
    return ("IMPOSSIBLE", False)
  else:
    return (rank, True)

# 입력
results = []

for _ in range(int(input())):
  N = int(input())
  graph = [[False] * (N + 1) for _ in range(N + 1)]
  entry_list = [0] * (N + 1)

  rank = list(map(int, input().split()))

  # 초기화
  for i in range(N):
    for j in range(i + 1, N):
      graph[rank[i]][rank[j]] = True  # rank[i]가 rank[j]보다 높은(좋은) 순위 rank[i]->rank[j]
      entry_list[rank[j]] += 1

  M = int(input())
  for _ in range(M):
    a, b = map(int, input().split())  # a->b / a가 b보다 높은 순위
    if not graph[a][b]:
      graph[a][b] = True
      entry_list[b] += 1
      graph[b][a] = False
      entry_list[a] -= 1
    else:
      graph[b][a] = True
      entry_list[a] += 1
      graph[a][b] = False
      entry_list[b] -= 1

  results.append(topology_sort(graph, entry_list, N))

for result, available in results:
  if available:
    for node in result:
      print(node, end=' ')
    print("")
  else:
    print(result)
