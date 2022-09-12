import heapq
import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def findStartEndPt(graph):
    start = (0,0)
    end = (0,0)
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 'S':
                start = (i, j)
            elif graph[i][j] == 'F':
                end = (i, j)
    return start, end

def checkNearest(graph):
    global di, dj
    W, H = len(graph[0]), len(graph)
    for i in range(H):
        for j in range(W):
            if graph[i][j] != 'g':
                continue
            # 쓰레기장이면
            for dirIdx in range(4):
                ni = i + di[dirIdx]
                nj = j + dj[dirIdx]
                if not (0 <= ni < H and 0 <= nj < W):
                    continue
                if not (graph[ni][nj] == '.'):
                    continue
                graph[ni][nj] = 'n'

def dijkstra(startPt, endPt, graph):
    global di, dj
    W, H = len(graph[0]), len(graph)
    INF = int(1e10)
    distance = [[(INF, INF) for _ in range(W)] for _ in range(H)]
    hp = [((0, 0), startPt)]
    distance[startPt[0]][startPt[1]] = (0, 0)
    result = []
    while hp:
        cost, curPt = heapq.heappop(hp)
        tp, tnp = cost
        ci, cj = curPt
        if distance[curPt[0]][curPt[1]] < cost:
            continue
        
        for dirIdx in range(4):
            ni = ci + di[dirIdx]
            nj = cj + dj[dirIdx]
            if not (0 <= ni < H and 0 <= nj < W):
                continue

            newTp = tp + 1 if graph[ni][nj] == 'g' else tp
            newTnp = tnp + 1 if graph[ni][nj] == 'n' else tnp
            
            if (newTp, newTnp) < distance[ni][nj]:
                distance[ni][nj] = (newTp, newTnp)
                heapq.heappush(hp, ((newTp, newTnp), (ni, nj)))
    return distance[endPt[0]][endPt[1]]
            
N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]

startPt, endPt = findStartEndPt(graph)
checkNearest(graph)

trashPassed, trashNearPassed = dijkstra(startPt, endPt, graph)
print(trashPassed, trashNearPassed)