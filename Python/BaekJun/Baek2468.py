from collections import deque
import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def getIslandCnt(graph, N, waterLevel):
    visited = [[False for _ in range(N)] for _ in range(N)]
    totalCnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            if graph[i][j] <= waterLevel:
                continue
            totalCnt += 1
            start = (i, j) # i, j
            visited[i][j] = True
            q = deque([start])
            while q:
                ci, cj = q.popleft()
                for idx in range(4):
                    ni = ci + di[idx]
                    nj = cj + dj[idx]
                    if not (0 <= ni < N and 0 <= nj < N):
                        continue
                    if visited[ni][nj]:
                        continue
                    if graph[ni][nj] <= waterLevel:
                        continue
                    visited[ni][nj] = True
                    q.append((ni, nj))
    return totalCnt

maxHeight = max([max(line) for line in graph])
maxIslandCnt = 0
for h in range(maxHeight + 1):
    maxIslandCnt = max(maxIslandCnt, getIslandCnt(graph, N, h))

print(maxIslandCnt)