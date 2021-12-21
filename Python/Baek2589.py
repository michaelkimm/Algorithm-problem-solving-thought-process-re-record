from collections import deque

# 입력 받기
# 미로 크기
N, M = map(int, input().split())

# 미로
graph = []
for _ in range(N):
  graph.append(list(input()))

# 거리 계산 맵
distMap = [[-1] * len(graph[0]) for _ in range(len(graph))]

maxDist = 0
# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj, graph_, distMap_):
  global di, dj

  # 큐 생성
  queue = deque([(si, sj)])

  # 방문 처리
  distMap_[si][sj] = 0
  maxVal = 0
  secondMaxVal = -1

  while queue:
    # 하나 꺼내기
    ci, cj = queue.popleft()

    # 주변 노드들
    for i in range(4):
      ni = ci + di[i]
      nj = cj + dj[i]
      
      # 접근 불가면
      if ni < 0 or ni > len(graph_) - 1 or nj < 0 or nj > len(graph_[0]) - 1:
        continue
      if (graph_[ni][nj] == 'W'):
        continue
      
      # 방문 안했으면
      if distMap_[ni][nj] == -1:
        # 큐 삽입
        queue.append((ni, nj))
        # 방문 처리
        distMap_[ni][nj] = distMap_[ci][cj] + 1
        maxVal = max(maxVal, distMap_[ni][nj])

  return maxVal

for i in range(N):
  for j in range(M):
    if distMap[i][j] == -1 and graph[i][j] == 'L':
      maxDist = max(maxDist, bfs(i, j, graph, distMap))
      distMap = [[-1] * len(graph[0]) for _ in range(len(graph))]

print(maxDist)
