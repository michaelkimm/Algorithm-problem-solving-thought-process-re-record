# 입력
N, L, R = map(int, input().split())
graph = []
groupGraph = []

groupTotal = [0] * (N * N)
groupCount = [0] * (N * N)
visited = []
for _ in range(N):
  graph.append(list(map(int, input().split())))
visited = [[False] * N for _ in range(N)]
groupGraph = [[-1] * N for _ in range(N)]

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(ci, cj, graph_, visited_, groupIdx_, groupGraph_, groupTotal_, groupCount_):
  global di, dj, L, R
  # 방문 처리
  visited_[ci][cj] = True    

  # 그룹 부여
  groupGraph_[ci][cj] = groupIdx_

  # 해당 그룹 숫자 + 1
  groupCount_[groupIdx_] = groupCount_[groupIdx_] + 1
    
  # 해당 그룹 총합 계산
  groupTotal_[groupIdx_] = groupTotal_[groupIdx_] + graph_[ci][cj]

  # 인접 노드 순환
  for i in range(4):
    ni = ci + di[i]
    nj = cj + dj[i]
    # 접근 불가능한가
    if ni < 0 or ni > len(graph_) - 1 or nj < 0 or nj > len(graph_[0]) - 1:
      continue
    # 방문 했다면
    if visited_[ni][nj]:
      continue
    # 영역 확장 가능하다면
    if abs(graph_[ni][nj] - graph_[ci][cj]) >= L and abs(graph_[ni][nj] - graph_[ci][cj]) <= R:
      dfs(ni, nj, graph_, visited_, groupIdx_, groupGraph_, groupTotal_, groupCount_)



result = 0
groupIdx = 0
while True:
  for i in range(N):
    for j in range(N):
        # dfs or bfs make group, calculate mean value
        if not visited[i][j]:
          dfs(i, j, graph, visited, groupIdx, groupGraph, groupTotal, groupCount)
          groupIdx += 1

  for i in range(N):
      for j in range(N):
        # 특정 그룹에 속하면
        if groupGraph[i][j] != -1:
            # 값을 업데이트
            graph[i][j] = int(groupTotal[groupGraph[i][j]] / groupCount[groupGraph[i][j]])     

  # 그룹 없으면 종료
  if groupIdx == N * N:
      break
  # 초기화
  for i in range(N):
    for j in range(N):
      visited[i][j] = False
      groupTotal[i * N + j] = 0
      groupCount[i * N + j] = 0
      groupGraph[i][j] = -1
  
  result += 1
  groupIdx = 0

print(result)

