from collections import deque
import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]

def getKeyFromGraph(keyCnt, graph, i, j):
    key = graph[i][j]
    idx = ord(key) - ord('a')
    return keyCnt[:idx] + '1' + keyCnt[idx+1:]

def getDoorToKey(doorType):
    return doorType.lower()

def checkKeyExists(keyCnt, doorType):
    return keyCnt[ord(getDoorToKey(doorType)) - ord('a')] == '1'

def getStartPt(graph, N, M):
    ret = (0, 0)
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == '0':
                ret = (i, j)
                break
    return ret

def bfs(startPt, graph):
    global di, dj, N, M
    keys = set(['a', 'b', 'c', 'd', 'e', 'f'])
    doors = set(['A', 'B', 'C', 'D', 'E', 'F'])
    keyCnt = "000000"
    moveCnt = 0
    q = deque([(startPt[0], startPt[1], moveCnt, keyCnt)])
    # visited = i, j, moveCnt, keyCnt
    visited = [[[False for _ in range(6)] for _ in range(M)] for _ in range(N)]
    
    ret = -1
    while q:
        ci, cj, moveCnt, keyCnt = q.popleft()
        if graph[ci][cj] == '1':
            ret = moveCnt
            break

        for dirIdx in range(4):
            ni, nj = ci + di[dirIdx], cj + dj[dirIdx]
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if graph[ni][nj] == '#':
                continue

            newKeyCnt = keyCnt[:1] + '' + keyCnt[1:]

            # 키인 경우
            if graph[ni][nj] in keys:
                newKeyCnt = getKeyFromGraph(newKeyCnt, graph, ni, nj)
            # 문인 경우
            elif graph[ni][nj] in doors:
                doorType = graph[ni][nj]
                if not checkKeyExists(newKeyCnt, doorType):
                    continue
            if visited[ni][nj][]:
                continue
            q.append((ni, nj, moveCnt + 1, newKeyCnt))
            visited[ni][nj] = True
                    
                
    return ret

startPt = getStartPt(graph, N, M)
result = bfs(startPt, graph)
print(result)

