import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)] 

def spreadDust(graph):
    global R, C, di, dj
    tempGraph = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            # 청정기 자리는 pass, 먼지 없는 경우도 pass
            if graph[i][j] == -1 or graph[i][j] == 0:
                continue
            spreadedCnt = 0
            spreadAmount = graph[i][j] // 5 
            for idx in range(4):
                ni = i + di[idx]
                nj = j + dj[idx]
                if not (0 <= ni < R and 0 <= nj < C):
                    continue
                if graph[ni][nj] == -1:
                    continue
                tempGraph[ni][nj] += spreadAmount
                spreadedCnt += 1
            graph[i][j] -= (spreadedCnt * spreadAmount)

    for i in range(R):
        for j in range(C):
            graph[i][j] += tempGraph[i][j] 
    return

def turnOnAirCleaner(graph):
    global R, C, di, dj

def getAirCleanerPose(graph):
    global R, C
    ret = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] == -1:
                ret.append((i, j))
    return ret

def getAirPathPoses(graph, airCleanerPose, CW):
    global R, C
    ret = []
    ai = airCleanerPose[0]
    aj = airCleanerPose[1]
    if CW:
        # 우
        for j in range(1, C):
            ret.append((ai, j))
        # 하
        for i in range(ai + 1, R):
            ret.append((i, C - 1))
        # 좌
        for j in range(C - 2, -1, -1):
            ret.append((R - 1, j))
        # 상
        for i in range(R - 2, ai, -1):
            ret.append((i, 0))
    else:
        # 우
        for j in range(1, C):
            ret.append((ai, j))
        # 상
        for i in range(ai - 1, -1, -1):
            ret.append((i, C - 1))
        # 좌
        for j in range(C - 2, -1, -1):
            ret.append((0, j))
        # 하
        for i in range(1, ai):
            ret.append((i, 0))
    return ret

def getDustAmounts(dustPoses, graph):
    ret = []
    for i, j in dustPoses:
        ret.append(graph[i][j])
    return ret

def cleanDusts(poses, graph):
    for i, j in poses:
        graph[i][j] = 0
    return

def setDusts(poses, dusts, graph):
    for idx, (i, j) in enumerate(poses):
        graph[i][j] = dusts[idx]
    return 

def turnOnAirCleaner(graph):
    airCleanerPoses = getAirCleanerPose(graph)
    airCleanerUpPose = airCleanerPoses[0]
    
    # 반시계 청소
    airPathPoses = getAirPathPoses(graph, airCleanerUpPose, CW = False)
    dustAmounts = getDustAmounts(airPathPoses, graph)
    cleanDusts(airPathPoses, graph)
    airPathPoses.pop(0)
    setDusts(airPathPoses, dustAmounts, graph)

    # 시계 청소
    airCleanerDownPose = airCleanerPoses[1]
    airPathPoses = getAirPathPoses(graph, airCleanerDownPose, CW = True)
    dustAmounts = getDustAmounts(airPathPoses, graph)
    cleanDusts(airPathPoses, graph)
    airPathPoses.pop(0)
    setDusts(airPathPoses, dustAmounts, graph)

def getDustLeft(graph):
    global R, C
    ret = 0
    for i in range(R):
        for j in range(C):
            if 1 <= graph[i][j]:
                ret += graph[i][j]
    return ret


while T >= 1:
    T -= 1
    spreadDust(graph)
    turnOnAirCleaner(graph)

print(getDustLeft(graph))