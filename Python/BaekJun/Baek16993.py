from collections import deque
import sys
input = sys.stdin.readline

# 동,서,남,북,제자리
di = [0, 0, 1, -1, 0]
dj = [1, -1, 0, 0, 0]

N, M, K = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

def bfs(graph, K):
    global di, dj, N, M
    moveCnt = 1
    startPt = (0, 0)
    # 낮=1, 밤=0
    state = 1
    q = deque([(startPt[0], startPt[1], moveCnt, K, state)])
    # visited = i, j, graph, moveCnt
    visited = [[[[False for _ in range(2)] for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
    visited[startPt[0]][startPt[1]][K][state] = True

    ret = -1
    while q:
        ci, cj, moveCnt, K, state = q.popleft()
        if ci == N - 1 and cj == M - 1:
            ret = moveCnt
            break

        for dirIdx in range(5):
            ni, nj = ci + di[dirIdx], cj + dj[dirIdx]
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            
            newK = K
            
            if graph[ni][nj] == 1:
                if newK == 0:
                    continue
                elif state == 1 and newK >= 1:
                    newK -= 1
                elif state == 0:
                    continue

            newState = 1 if state == 0 else 0

            if visited[ni][nj][newK][newState]:
                continue
            q.append((ni, nj, moveCnt + 1, newK, newState))
            visited[ni][nj][newK][newState] = True
                    
    return ret

result = bfs(graph, K)
print(result)