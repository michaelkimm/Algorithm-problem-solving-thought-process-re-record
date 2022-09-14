from collections import deque
import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N, M, K = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

def bfs(graph, K):
    global di, dj, N, M
    moveCnt = 1
    startPt = (0, 0)
    q = deque([(startPt[0], startPt[1], moveCnt, K)])
    # visited = i, j, graph, moveCnt
    visited = [[[False for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
    visited[startPt[0]][startPt[1]][K] = True

    ret = -1
    while q:
        ci, cj, moveCnt, K = q.popleft()
        if ci == N - 1 and cj == M - 1:
            ret = moveCnt
            break

        for dirIdx in range(4):
            ni, nj = ci + di[dirIdx], cj + dj[dirIdx]
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            
            newK = K
            
            if graph[ni][nj] == 1:
                if newK == 0:
                    continue
                elif newK >= 1:
                    newK -= 1

            if visited[ni][nj][newK]:
                continue
            q.append((ni, nj, moveCnt + 1, newK))
            visited[ni][nj][newK] = True
                    
    return ret

result = bfs(graph, K)
print(result)