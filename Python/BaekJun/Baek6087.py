import heapq
import sys
input = sys.stdin.readline

# 동서남북
# 동=0,남=1,서=2,북=3
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def findCfromGraph(graph):
    W, H = len(graph[0]), len(graph)
    target = []
    cCount = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 'C':
                target.append((i, j))

    return target[0], target[1]

def dijkstra(startPt, endPt, graph):
    global di, dj

    W, H = len(graph[0]), len(graph)
    INF = int(1e10)
    distance = [[INF for _ in range(W)] for _ in range(H)]
    distance[startPt[0]][startPt[1]] = 0
    hp = []
    for dirIdx in range(4):
        heapq.heappush(hp, (0, startPt, dirIdx))
    while hp:
        dist, curPt, curDir = heapq.heappop(hp)
        ci, cj = curPt
        if distance[ci][cj] < dist:
            continue
        if curPt == endPt:
            break

        for dirIdx in range(4):
            ni = ci + di[dirIdx]
            nj = cj + dj[dirIdx]
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if graph[ni][nj] == '*':
                continue
            # 반대인 경우
            if curDir == (dirIdx + 2) % 4:
                continue
            # 직진일 경우
            elif curDir == dirIdx:
                newDist = distance[ci][cj]
                if distance[ni][nj] >= newDist:
                    nextDir = curDir
                    distance[ni][nj] = newDist
                    heapq.heappush(hp, (newDist, (ni, nj), nextDir))
            # 90도 꺾기일 경우
            else:
                newDist = distance[ci][cj] + 1
                if distance[ni][nj] >= newDist:
                    nextDir = dirIdx
                    distance[ni][nj] = newDist
                    heapq.heappush(hp, (newDist, (ni, nj), nextDir))

    return distance[endPt[0]][endPt[1]]

W, H = map(int, input().split())
graph = [[v for v in str(input().strip())] for _ in range(H)]


startPt, endPt = findCfromGraph(graph)

minMirrorCnt = dijkstra(startPt, endPt, graph)
print(minMirrorCnt)