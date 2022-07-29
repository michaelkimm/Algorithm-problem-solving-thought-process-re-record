import sys
input = sys.stdin.readline

# →, ←, ↑, ↓
di = [0, 0, -1 , 1]
dj = [1, -1, 0, 0]

N, K = map(int, input().split())
# 0은 흰색, 1은 빨간색, 2는 파란색
colorGraph = [list(map(int, input().split())) for _ in range(N)]
horsePoses = [(-1, -1) for _ in range(K + 1)]
stackedGraph = [[[] for _ in range(N)] for _ in range(N)]
horseDirs = [-1 for _ in range(K + 1)]
targetStackedHeight = 4

for horseNum in range(1, K + 1):
    i, j, direction = map(int, input().split())
    i -= 1
    j -= 1
    direction -= 1
    horsePoses[horseNum] = (i, j)
    stackedGraph[i][j].append(horseNum)
    horseDirs[horseNum] = direction

def flipStacked(horseNum):
    orgBottom = horseNum
    hi, hj = horsePoses[orgBottom]
    orgStacked = stackedGraph[hi][hj]
    horseIdxInStakced = orgStacked.index(horseNum)
    flipTargetStacked = orgStacked[horseIdxInStakced:]
    flipedStack = flipTargetStacked[::-1]

    # 새롭게 올릴 스택 만들기
    newStacked = orgStacked[:horseIdxInStakced]
    newStacked.extend(flipedStack)

    # 만들어진 새 스택으로 업데이트
    stackedGraph[hi][hj] = newStacked
    newBottom = flipedStack[0]
    return newBottom

def getNextPose(horseNum, horsePoses, horseDir):
    ni = horsePoses[horseNum][0] + di[horseDir[horseNum]]
    nj = horsePoses[horseNum][1] + dj[horseDir[horseNum]]
    return ni, nj

def isInBoundary(ni, nj):
    return 0 <= ni < N and 0 <= nj < N

def getReverseDirection(direction):
    # →, ←, ↑, ↓
    if direction == 0: return 1
    elif direction == 1: return 0
    elif direction == 2: return 3
    else: return 2

def moveHorse(ti, tj, horseNum):
    hi, hj = horsePoses[horseNum]
    horseStackedIdx = stackedGraph[hi][hj].index(horseNum)
    targetMovableStacked = stackedGraph[hi][hj][horseStackedIdx:]

    # 현재 위치에서 옮겨질 탑 제거
    stackedGraph[hi][hj] = stackedGraph[hi][hj][:horseStackedIdx]

    # 옮겨질 위치에 탑 쌓기
    stackedGraph[ti][tj].extend(targetMovableStacked)

    # horsePoses 업데이트
    for movedHorseNum in targetMovableStacked:
        horsePoses[movedHorseNum] = (ti, tj)
    
    return len(stackedGraph[ti][tj]) >= targetStackedHeight

def moveHorseWithoutBlueColorRule(ti, tj, horseNum):
    # 다음 칸 색이 빨강인 경우
    if colorGraph[ti][tj] == 1:
        horseNum = flipStacked(horseNum)
    return moveHorse(ti, tj, horseNum)

def moveHorseWithBlueColorRule(horseNum):
    ni = horsePoses[horseNum][0] + di[horseDirs[horseNum]]
    nj = horsePoses[horseNum][1] + dj[horseDirs[horseNum]]
    if not isInBoundary(ni, nj) or colorGraph[ni][nj] == 2:
        # 방향 반대, 한칸 전진 시도.
        horseDirs[horseNum] = getReverseDirection(horseDirs[horseNum])
        ni, nj = getNextPose(horseNum, horsePoses, horseDirs)
        if not isInBoundary(ni, nj) or colorGraph[ni][nj] == 2:
            return False

    return moveHorseWithoutBlueColorRule(ni, nj, horseNum)

def isMaxStackedHeightHigherThan(height):
    for horseNum in range(1, K + 1):
        i, j = horsePoses[horseNum]
        if len(stackedGraph[i][j]) >= height:
            return True
    return False
    
time = 0
foundAnswer = False
while True:
    if time > 1000:
        time = -1
        break

    time += 1
    for horseNum in range(1, K + 1):
        result = moveHorseWithBlueColorRule(horseNum)
        if result:
            foundAnswer = True
            break
    if foundAnswer:
        break
    
print(time)