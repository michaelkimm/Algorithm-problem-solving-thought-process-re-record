from collections import deque
import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N, M, K = map(int, input().split())
graph = ''
for _ in range(N):
    graph += input().strip()

def getGraphElement(graph, i, j):
    global N, M
    return graph[i * M + j]


def breakWall(graph, i, j):
    global N, M
    return graph[:i * M + j] + '0' + graph[i * M + j + 1:]

def bfs(graph, K):
    global di, dj, N, M
    moveCnt = 1
    startPt = (0, 0)
    q = deque([(startPt[0], startPt[1], moveCnt, K)])
    # visited = i, j, graph, moveCnt
    visited = set([(startPt[0], startPt[1], K)])

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
            
            if getGraphElement(graph, ni, nj) == '1':
                if K == 0:
                    continue
                else:
                    newK -= 1

            if (ni, nj, newK) in visited:
                continue
            q.append((ni, nj, moveCnt + 1, newK))
            visited.add((ni, nj, newK))
                    
    return ret

result = bfs(graph, K)
print(result)