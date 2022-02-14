import sys
input = sys.stdin.readline

INF = int(1e9)

# 입력
N, M = map(int, input().split())

distance = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  u, v = map(int, input().split())
  distance[u][v] = 1
X, K = map(int, input().split())

# 자기자신까지 거리 0
for i in range(1, N + 1):
  distance[i][i] = 0

# 플로이드 워셜
for mid in range(N + 1):
  for i in range(N + 1):
    for j in range(N + 1):
      distance[i][j] = min(distance[i][j], distance[i][mid] + distance[mid][j])

result = min(distance[1][K], distance[K][1]) + min(distance[K][X], distance[X ][K])
if result >= INF:
  print(-1)
else:
  print(result)

####################################################################

import sys
input = sys.stdin.readline

INF = int(1e9)

# 입력
N, M = map(int, input().split())

distance = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  u, v = map(int, input().split())
  distance[u][v] = 1
  distance[v][u] = 1
X, K = map(int, input().split())

# 자기자신까지 거리 0
for i in range(1, N + 1):
  distance[i][i] = 0

# 플로이드 워셜
for mid in range(N + 1):
  for i in range(N + 1):
    for j in range(N + 1):
      distance[i][j] = min(distance[i][j], distance[i][mid] + distance[mid][j])

result = distance[1][K] + distance[K][X]
if result >= INF:
  print(-1)
else:
  print(result)

