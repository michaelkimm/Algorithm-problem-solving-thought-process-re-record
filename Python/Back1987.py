import sys

H, W = map(int, sys.stdin.readline().split())
graph = []
for _ in range(H):
  graph.append(list(sys.stdin.readline().strip()))

maxDist = 0

# 상하좌우
di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

# bfs
queue = set()
queue.add((0, 0, graph[0][0]))

# 방문 처리

while queue:
  ci, cj, string = queue.pop()
  
  maxDist = max(maxDist, len(string))
  if maxDist == 26:
    break

  # 인접 노드 방문
  for i in range(4):
    ni = ci + di[i]
    nj = cj + dj[i]

    if ni < 0 or ni >= H or nj < 0 or nj >= W:
      continue
    if graph[ni][nj] not in string:
      queue.add((ni, nj, string + graph[ni][nj]))   

print(maxDist)