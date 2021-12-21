# 입력 받기
N, M = map(int, input().split())
iceMap = []
for _ in range(N):
  iceMap.append(list(map(int, input())))

def dfs(i, j, graph):
  global N, M

  if (i < 0 or i > N - 1 or j < 0 or j > M - 1):
    return
  if graph[i][j] == 1:
    return

  graph[i][j] = 1
  dfs(i, j - 1, graph)
  dfs(i, j + 1, graph)
  dfs(i - 1, j, graph)
  dfs(i + 1, j, graph)

iceCreamCnt = 0

for i in range(N):
  for j in range(M):
    if iceMap[i][j] == 0:
      dfs(i, j, iceMap)
      iceCreamCnt += 1

print(iceCreamCnt)