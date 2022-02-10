from collections import deque
import sys
input = sys.stdin.readline

# 입력
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
entryCnt = [0 for _ in range(V + 1)]

for _ in range(E):
  u, v = map(int, input().split())
  graph[u].append(v)
  entryCnt[v] += 1

def topology_sort():
  q = deque()
  result = []

  for node in range(1, V + 1):
    if entryCnt[node] == 0:
      q.appendleft(node)

  while q:
    node = q.popleft()
    result.append(node)
    for v in graph[node]:

      entryCnt[v] -= 1
      if entryCnt[v] == 0:
        q.appendleft(v)

  print(result)

topology_sort()
