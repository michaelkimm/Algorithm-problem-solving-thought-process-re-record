from collections import defaultdict
import sys
input = sys.stdin.readline

# 상=1, 하=2, 좌=3, 우=4
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

def processTimePassed(smellGraph):
    global N, K
    for i in range(N):
        for j in range(N):
            if smellGraph[i][j] != []:
                smellGraph[i][j] = [smellGraph[i][j][0], smellGraph[i][j][1] - 1]
                if smellGraph[i][j][1] == 0:
                    smellGraph[i][j] = []

def spreadSmell(sharkGraph, smellGraph):
    global N, K
    for i in range(N):
        for j in range(N):
            if sharkGraph[i][j] != []:
                smellGraph[i][j] = [sharkGraph[i][j][0], K]

def moveShark(sharkNum, sharkDirs, sharkGraph, sharkPoses, toRow, toCol, toDir):
    sharkGraph[toRow][toCol].append(sharkNum)
    sharkPoses[sharkNum] = [toRow, toCol]
    sharkDirs[sharkNum] = toDir

def processMultipleSharkInNode(sharkGraph, sharkPoses):
    global N
    # 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
    for i in range(N):
        for j in range(N):
            if len(sharkGraph[i][j]) >= 2:
                survivableSharkNum = min(sharkGraph[i][j])
                sharkGraph[i][j].remove(survivableSharkNum)

                # 쫒아내기
                for kickedSharkNum in sharkGraph[i][j]:
                    sharkPoses[kickedSharkNum] = []
                
                sharkGraph[i][j] = [survivableSharkNum]

def moveAllShark(smellGraph, sharkDirs, sharkPoses):
    global N, M, sharkDirSeq, di, dj
    newSharkGraph = [[[] for _ in range(N)] for _ in range(N)]
    # 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동
    for sharkNum in range(1, M + 1):
        if sharkPoses[sharkNum] == []:
            continue
        # 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
        foundNonSmellZone = False
        for dir in sharkDirSeq[sharkNum][sharkDirs[sharkNum]]:
            ni = sharkPoses[sharkNum][0] + di[dir]
            nj = sharkPoses[sharkNum][1] + dj[dir]
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if smellGraph[ni][nj] == []:
                moveShark(sharkNum, sharkDirs, newSharkGraph, sharkPoses, ni, nj, dir)
                foundNonSmellZone = True
                break
        if foundNonSmellZone:
            continue
            
        # 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
        for dir in sharkDirSeq[sharkNum][sharkDirs[sharkNum]]:
            ni = sharkPoses[sharkNum][0] + di[dir]
            nj = sharkPoses[sharkNum][1] + dj[dir]
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if smellGraph[ni][nj][0] == sharkNum:
                moveShark(sharkNum, sharkDirs, newSharkGraph, sharkPoses, ni, nj, dir)
                break

    return newSharkGraph

def initialize(targetSharkGraph, targetSharkPoses, sourceSharkGraph):
    for i in range(N):
        for j in range(N):
            if sourceSharkGraph[i][j] != 0:
                targetSharkGraph[i][j].append(sourceSharkGraph[i][j])
                targetSharkPoses[sourceSharkGraph[i][j]] = [i, j]

def existOnlyOne(sharkPoses):
    global M
    return sharkPoses.count([]) == M

N, M, K = map(int, input().split())
inputSharkGraph = [list(map(int, input().split())) for _ in range(N)]
sharkGraph = [[[] for _ in range(N)] for _ in range(N)]
sharkPoses = [[] for _ in range(M + 1)]
initialize(sharkGraph, sharkPoses, inputSharkGraph)

sharkDirs = [0] 
sharkDirs.extend(list(map(int, input().split())))

sharkDirSeq = defaultdict(defaultdict)
for sharkNum in range(1, M + 1):
    sharkDirSeq[sharkNum][1] = list(map(int, input().split()))
    sharkDirSeq[sharkNum][2] = list(map(int, input().split()))
    sharkDirSeq[sharkNum][3] = list(map(int, input().split()))
    sharkDirSeq[sharkNum][4] = list(map(int, input().split()))



smellGraph = [[[] for _ in range(N)] for _ in range(N)]
timePassed = 0

# 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
spreadSmell(sharkGraph, smellGraph)

while not existOnlyOne(sharkPoses):
    sharkGraph = moveAllShark(smellGraph, sharkDirs, sharkPoses)
    processMultipleSharkInNode(sharkGraph, sharkPoses)
    processTimePassed(smellGraph)
    spreadSmell(sharkGraph, smellGraph)
    timePassed += 1
    if timePassed > 1000:
        timePassed = -1
        break

print(timePassed)