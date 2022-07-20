from collections import deque
import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def getFishInfos(graph, N):
    # fishInfos = (i, j, size)
    ret = []
    for i in range(N):
        for j in range(N):
            if 1 <= graph[i][j] <= 6:
                ret.append(i, j, graph[i][j])
    return ret

def isFish(info):
    return 1 <= info <= 6

def isEatable(fishSize, sharkSize):
    return sharkSize > fishSize

def getSharkPose(graph, N):
    sharkPose = (0, 0)
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                sharkPose = (i, j)
                graph[i][j] = 0
                break
    return sharkPose

def getEatablesQ(graph, sharkSize, sharkPose):
    global di, dj
    # fishInfos = (i, j, size)
    N = len(graph)
    eatables = []
    minDist = int(1e10)
    time = 0
    q = deque([(sharkPose, time)]) # (현재 위치, 상어 크기, 지나온 시간)
    visited = set([(sharkPose)])
    while q:
        sharkPose, time = q.popleft()
        ci, cj = sharkPose
        
        if isFish(graph[ci][cj]) and isEatable(graph[ci][cj], sharkSize):
            if time <= minDist:
                minDist = time
                eatables.append((minDist, ci, cj, graph[ci][cj]))
            else:
                break

        for idx in range(4):
            ni = ci + di[idx]
            nj = cj + dj[idx]
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if graph[ni][nj] > sharkSize:
                continue
            if ((ni, nj)) in visited:
                continue
            visited.add(((ni, nj)))
            q.append(((ni, nj), time + 1))

    eatables.sort()
    return deque(eatables)

# 아기 상어, 물고기 정보 구하기
sharkPose = getSharkPose(graph, N)
sharkSize = 2
fishNeedForGrowCnt = 2
time = 0
eatablesQ = getEatablesQ(graph, sharkSize, sharkPose)

cnt = 0 

while eatablesQ:
    eatable = eatablesQ.popleft()
    sharkToFishDist, fi, fj, fSize = eatable

    # 상어 움직이기
    sharkPose = (fi, fj)
    time += sharkToFishDist
    
    # 잡아먹기
    if isEatable(fSize, sharkSize):
        fishNeedForGrowCnt -= 1
        if fishNeedForGrowCnt == 0:
            sharkSize += 1
            fishNeedForGrowCnt = sharkSize
        graph[fi][fj] = 0
    eatablesQ = getEatablesQ(graph, sharkSize, sharkPose)

print(time)