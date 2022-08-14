import sys
input = sys.stdin.readline


# 방향 / 서남동북
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

N = int(input())
graph = [[ -1 for _ in range(N)] for _ in range(N)]

sandErasedAmount = 0

def getCWDir(curDir):
    return (curDir + 3) % 4

def getCCWDir(curDir):
    return (curDir + 1) % 4

def processSandMove(graph, ni, nj, ci, cj, val):
    global sandErasedAmount, N
    if (0 <= ni < N and 0 <= nj < N):
        graph[ni][nj] += val
    else:
        sandErasedAmount += val
    graph[ci][cj] -= val

def getLeftFront(ci, cj, curDir, leftCnt, frontCnt):
    global di, dj
    lfi = ci + di[getCCWDir(curDir)] * leftCnt + di[curDir] * frontCnt
    lfj = cj + dj[getCCWDir(curDir)] * leftCnt + dj[curDir] * frontCnt
    return lfi, lfj

def getRightFront(ci, cj, curDir, rightCnt, frontCnt):
    global di, dj
    rfi = ci + di[getCWDir(curDir)] * rightCnt + di[curDir] * frontCnt
    rfj = cj + dj[getCWDir(curDir)] * rightCnt + dj[curDir] * frontCnt
    return rfi, rfj

def blowSand(graph, pose):
    global sandErasedAmount, N
    ci, cj, curDir = pose
    ni, nj = ci + di[curDir], cj + dj[curDir]
    if not (0 <= ni < N and 0 <= nj < N):
        return
    moveNeedAmountOrg = graph[ni][nj]
    totalMoved = 0
    
    # CW : curDir + 3, CCW : curDir + 1
    # 좌우
    li, lj = getLeftFront(ci, cj, curDir, 1, 0)
    ri, rj = getRightFront(ci, cj, curDir, 1, 0)
    moveVal = moveNeedAmountOrg // 100
    processSandMove(graph, li, lj, ni, nj, moveVal)
    processSandMove(graph, ri, rj, ni, nj, moveVal)
    totalMoved += moveVal
    totalMoved += moveVal

    # 좌앞, 우앞
    lfi, lfj = getLeftFront(ci, cj, curDir, 1, 1)
    rfi, rfj = getRightFront(ci, cj, curDir, 1, 1)
    moveVal = int(moveNeedAmountOrg * 0.07)
    processSandMove(graph, lfi, lfj, ni, nj, moveVal)
    processSandMove(graph, rfi, rfj, ni, nj, moveVal)
    totalMoved += moveVal
    totalMoved += moveVal

    # 좌좌앞, 우우앞
    llfi, llfj = getLeftFront(ci, cj, curDir, 2, 1)
    rrfi, rrfj = getRightFront(ci, cj, curDir, 2, 1)
    moveVal = int(moveNeedAmountOrg * 0.02)
    processSandMove(graph, llfi, llfj, ni, nj, moveVal)
    processSandMove(graph, rrfi, rrfj, ni, nj, moveVal)    
    totalMoved += moveVal
    totalMoved += moveVal

    # 좌앞앞, 우앞앞
    lffi, lffj = getLeftFront(ci, cj, curDir, 1, 2)
    rffi, rffj = getRightFront(ci, cj, curDir, 1, 2)
    moveVal = int(moveNeedAmountOrg * 0.1)
    processSandMove(graph, lffi, lffj, ni, nj, moveVal)
    processSandMove(graph, rffi, rffj, ni, nj, moveVal)    
    totalMoved += moveVal
    totalMoved += moveVal

    # 앞앞앞
    fffi, fffj = getRightFront(ci, cj, curDir, 0, 3)
    moveVal = int(moveNeedAmountOrg * 0.05)
    processSandMove(graph, fffi, fffj, ni, nj, moveVal)
    totalMoved += moveVal

    # a = 나머지
    ai, aj = getRightFront(ci, cj, curDir, 0, 2)
    moveVal = moveNeedAmountOrg - totalMoved
    processSandMove(graph, ai, aj, ni, nj, moveVal)

def checkLeftBlank(graph, curPose):
    ci, cj, curDir = curPose
    nextDir = (curDir + 1) % 4
    ni, nj = ci + di[nextDir], cj + dj[nextDir]

    return False if not (0 <= ni < N and 0 <= nj < N) else graph[ni][nj] == -1

def moveForward(graph, pose):
    ci, cj, curDir = pose
    ni, nj = ci + di[curDir], cj + dj[curDir] 
    pose = (ni, nj, curDir)
    
    blowSand(graph, pose)

    return pose

def rotateCCW(pose):
    ci, cj, curDir = pose
    pose = (ci, cj, (curDir + 1) % 4)
    return pose


start = (N // 2, N // 2, 3) # i, j, dirIndex
curPose = start

while curPose[0] != 0 or curPose[1] != 0:
    print(curPose)
    if checkLeftBlank(graph, curPose):
        curPose = rotateCCW(curPose)
        curPose = moveForward(graph, curPose)
    else:
        curPose = moveForward(graph, curPose)




for line in graph:
    print(line)