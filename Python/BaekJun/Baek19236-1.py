import sys
input = sys.stdin.readline

# 북, 북서, 서, 남서, 남, 남동, 동, 북동
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]

def findFishPose(graph, fishValue):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j][0] == fishValue:
                return (i, j)
    return (-1, -1)

inputData = [list(map(int, input().split())) for _ in range(4)]
graph = []
for a1, b1, a2, b2, a3, b3, a4, b4 in inputData:
    graph.append([(a1, b1 - 1), (a2, b2 - 1), (a3, b3 - 1), (a4, b4 - 1)])
    
sharkDir = graph[0][0][1]
sharkPose = (0, 0)
eatenAmount = graph[0][0][0]
graph[0][0] = (-1, graph[0][0][1])


def print2DArray(ary):
    print("=================")
    for line in ary:
        print(line)

def clone2DArray(graph):
    return [[graph[i][j] for j in range(len(graph[0]))] for i in range(len(graph))]

def getSharkMovablePoses(graph, sharkPose):
    sharkDir = graph[sharkPose[0]][sharkPose[1]][1]
    result = []
    for moveCnt in range(1, 4):
        ni = sharkPose[0] + (di[sharkDir] * moveCnt)
        nj = sharkPose[1] + (dj[sharkDir] * moveCnt)
        if not (0 <= ni < 4 and 0 <= nj < 4):
            continue
        if graph[ni][nj][0] == 0:
            continue
        result.append((ni, nj))
    return result

def moveShark(graph, sharkPose, sharkMovablePose):
    graph[sharkPose[0]][sharkPose[1]] = (0, 0)
    graph[sharkMovablePose[0]][sharkMovablePose[1]] = (-1, graph[sharkMovablePose[0]][sharkMovablePose[1]][1])

def recursive(graph, sharkPose, eatenAmount):
    sharkMovablePoses = getSharkMovablePoses(graph, sharkPose)
    if not sharkMovablePoses:
        return eatenAmount
    results = [0]
    for sharkMovablePose in sharkMovablePoses:
        newGraph = clone2DArray(graph)
        fishValue = newGraph[sharkMovablePose[0]][sharkMovablePose[1]][0]
        moveShark(newGraph, sharkPose, sharkMovablePose)
        moveFishes(newGraph)
        results.append(recursive(newGraph, sharkMovablePose, eatenAmount + fishValue))
        
    
    return max(results)

def isFishMovable(graph, fishPose):
    fishDir = graph[fishPose[0]][fishPose[1]][1]
    ni = fishPose[0] + di[fishDir]
    nj = fishPose[1] + dj[fishDir]
    if not (0 <= ni < 4 and 0 <= nj < 4):
        return False
    if graph[ni][nj][0] == -1:
        return False
    return True

def spin(graph, fishPose):
    fishDir = graph[fishPose[0]][fishPose[1]][1]
    newFishDir = (fishDir + 1) % 8
    graph[fishPose[0]][fishPose[1]] = (graph[fishPose[0]][fishPose[1]][0], newFishDir)

def moveFish(graph, fishPose):
    f1i, f1j = fishPose
    f1Value = graph[f1i][f1j][0]
    f1Dir = graph[f1i][f1j][1]
    f2i = f1i + di[f1Dir]
    f2j = f1j + dj[f1Dir]
    f2Value = graph[f2i][f2j][0]
    f2Dir = graph[f2i][f2j][1]
    graph[f2i][f2j] = (f1Value, f1Dir)
    graph[f1i][f1j] = (f2Value, f2Dir)

def moveFishes(graph):
    for fishValue in range(1, 17):
        fishPose = findFishPose(graph, fishValue)
        if fishPose == (-1, -1):
            continue
        spinnedCnt = 0
        while not isFishMovable(graph, fishPose) and spinnedCnt < 8:
            spin(graph, fishPose)
            spinnedCnt += 1
        
        if spinnedCnt >= 8:
            continue
        if isFishMovable(graph, fishPose):
            moveFish(graph, fishPose)

print(recursive(graph, sharkPose, eatenAmount))