import sys
input = sys.stdin.readline


# 방향 / 서남동북
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

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
    moveNeedAmountOrg = graph[ci][cj]
    totalMoved = 0
    
    # CW : curDir + 3, CCW : curDir + 1
    # 좌뒤, 우뒤
    lbi, lbj = getLeftFront(ci, cj, curDir, 1, -1)
    rbi, rbj = getRightFront(ci, cj, curDir, 1, -1)
    moveVal = moveNeedAmountOrg // 100
    processSandMove(graph, lbi, lbj, ci, cj, moveVal)
    processSandMove(graph, rbi, rbj, ci, cj, moveVal)
    totalMoved += moveVal
    totalMoved += moveVal
    # 좌, 우
    li, lj = getLeftFront(ci, cj, curDir, 1, 0)
    ri, rj = getRightFront(ci, cj, curDir, 1, 0)
    moveVal = int(moveNeedAmountOrg * 0.07)
    processSandMove(graph, li, lj, ci, cj, moveVal)
    processSandMove(graph, ri, rj, ci, cj, moveVal)
    totalMoved += moveVal
    totalMoved += moveVal
    # 좌좌, 우우
    lli, llj = getLeftFront(ci, cj, curDir, 2, 0)
    rri, rrj = getRightFront(ci, cj, curDir, 2, 0)
    moveVal = int(moveNeedAmountOrg * 0.02)
    processSandMove(graph, lli, llj, ci, cj, moveVal)
    processSandMove(graph, rri, rrj, ci, cj, moveVal)
    totalMoved += moveVal
    totalMoved += moveVal
    # 좌앞, 우앞
    lfi, lfj = getLeftFront(ci, cj, curDir, 1, 1)
    rfi, rfj = getRightFront(ci, cj, curDir, 1, 1)
    moveVal = int(moveNeedAmountOrg * 0.10)
    processSandMove(graph, lfi, lfj, ci, cj, moveVal)
    processSandMove(graph, rfi, rfj, ci, cj, moveVal)
    totalMoved += moveVal
    totalMoved += moveVal
    # 앞앞
    ffi, ffj = getLeftFront(ci, cj, curDir, 0, 2)
    moveVal = int(moveNeedAmountOrg * 0.05)
    processSandMove(graph, ffi, ffj, ci, cj, moveVal)
    totalMoved += moveVal
    # a = 나머지
    ai, aj = getLeftFront(ci, cj, curDir, 0, 1)
    moveVal = moveNeedAmountOrg - totalMoved
    processSandMove(graph, ai, aj, ci, cj, moveVal)

def checkLeftBlank(graph, curPose):
    global visited
    ci, cj, curDir = curPose
    nextDir = getCCWDir(curDir)
    ni, nj = ci + di[nextDir], cj + dj[nextDir]

    return False if not (0 <= ni < N and 0 <= nj < N) else (not visited[ni][nj])

def moveForward(graph, pose):
    global visited, N
    ci, cj, curDir = pose
    ni, nj = ci + di[curDir], cj + dj[curDir] 
    if not(0 <= ni < N and 0 <= nj < N):
        return pose

    newPose = (ni, nj, curDir)
    blowSand(graph, newPose)
   
    visited[ni][nj] = True
    
    return newPose

def rotateCCW(pose):
    ci, cj, curDir = pose
    pose = (ci, cj, (curDir + 1) % 4)
    return pose


start = (N // 2, N // 2, 3) # i, j, dirIndex
curPose = start
visited[start[0]][start[1]] = True

cnt = 0

while curPose[0] != 0 or curPose[1] != 0:
    if checkLeftBlank(graph, curPose):
        curPose = rotateCCW(curPose)
        curPose = moveForward(graph, curPose)
    else:
        curPose = moveForward(graph, curPose)

print(sandErasedAmount)  