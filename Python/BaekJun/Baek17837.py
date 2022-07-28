import sys
input = sys.stdin.readline

# →, ←, ↑, ↓
di = [0, 0, -1 , 1]
dj = [1, -1, 0, 0]

N, K = map(int, input().split())
# 0은 흰색, 1은 빨간색, 2는 파란색
colorGraph = [list(map(int, input().split())) for _ in range(N)]
horseGraph = [[0 for _ in range(N)] for _ in range(N)]

horseDirs = [-1] * (K + 1)
horsePoses = [(0,0)] * (K + 1)
horseOnAnother = [False] * (K + 1)
horseLayers = [[] for _ in range(K + 1)]
for horseNum in range(1, K + 1):
    i, j, direction = map(int, input().split())
    horseDirs[horseNum] = direction - 1
    horsePoses[horseNum] = (i - 1, j - 1)
    horseGraph[i - 1][j - 1] = horseNum


def getReverseDirection(direction):
    # →, ←, ↑, ↓
    if direction == 0: return 1
    elif direction == 1: return 0
    elif direction == 2: return 3
    else: return 2

def moveSingleHorse(horseNum, ti, tj, horsePoses, horseLayers, horseOnAnother):
    # 타겟 칸에 말 있다고 가정
    toTop = True
    # 타겟 칸에 말 없는 경우
    if horseGraph[ti][tj] == 0:
        toTop = False

    bi = horsePoses[horseNum][0]
    bj = horsePoses[horseNum][1]
    # 현재 자리 비우기
    horseGraph[bi][bj] = 0
    # 위치 옮기기
    if not toTop:
        horseGraph[ti][tj] = horseNum
    else:
        horseLayers[horseGraph[ti][tj]].extend([horseNum] + horseLayers[horseNum])
        horseLayers[horseNum] = []
        horseOnAnother[horseNum] = True
    horsePoses[horseNum] = (ti, tj)
    # 타고 있는 말도 위치 옮기기
    for horseOnhorse in horseLayers[horseNum]:
        horsePoses[horseOnhorse] = (ti, tj)

def reverseHorseComposition(horseNum, horseLayers, horsePoses, horseGraph, horseOnAnother):
    beforeBottom = horseNum
    layer = [horseNum]
    layer.extend(horseLayers[horseNum])
    reversedLayer = layer[::-1]
    newBottom = reversedLayer.pop(0)

    # 이전 horse 흔적 지우기
    horseLayers[beforeBottom] = []
    horseOnAnother[beforeBottom] = True
    # 새로운 bottom 설정
    horseLayers[newBottom] = reversedLayer
    horseOnAnother[newBottom] = False
    horseGraph[horsePoses[beforeBottom][0]][horsePoses[beforeBottom][1]] = newBottom
    return newBottom

def moveTo(ti, tj, horseNum, horsePoses, horseOnAnother, horseLayers, horseGraph):
    if colorGraph[ti][tj] == 1:
        # A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
        horseNum = reverseHorseComposition(horseNum, horseLayers, horsePoses, horseGraph, horseOnAnother)
        # print("reversed!")
        # printState(horsePoses, horseOnAnother, horseLayers)

    moveSingleHorse(horseNum, ti, tj, horsePoses, horseLayers, horseOnAnother)

def getNextPose(horseNum, horsePoses, horseDir):
    global di, dj
    ni = horsePoses[horseNum][0] + di[horseDir[horseNum]]
    nj = horsePoses[horseNum][1] + dj[horseDir[horseNum]]
    return ni, nj

def isInBoundary(ni, nj):
    return 0 <= ni < N and 0 <= nj < N

def moveSingleHorseWithColorRule(horseNum, horseDirs, horsePoses, horseOnAnother, horseLayers, horseGraph):
    global N, di, dj
    ni, nj = getNextPose(horseNum, horsePoses, horseDirs)

    if not isInBoundary(ni, nj) or colorGraph[ni][nj] == 2:
        # 방향 반대, 한칸 전진 시도.
        horseDirs[horseNum] = getReverseDirection(horseDirs[horseNum])
        nni, nnj = getNextPose(horseNum, horsePoses, horseDirs)
        if not isInBoundary(nni, nnj) or colorGraph[nni][nnj] == 2:
            return
        moveTo(nni, nnj, horseNum, horsePoses, horseOnAnother, horseLayers, horseGraph)
        return

    moveTo(ni, nj, horseNum, horsePoses, horseOnAnother, horseLayers, horseGraph)

def print2DArray(ary):
    for line in ary:
        print(line)
    print("=======================")

def printState(horsePoses, horseOnAnother, horseLayers):
    print("horsePoses")
    print(horsePoses)
    print("horseOnAnother")
    print(horseOnAnother)
    print("horseLayers")
    print(horseLayers)
    print("===================")

for horseNum in range(1, K + 1):
    if not horseOnAnother[horseNum]:
        # print(horseNum, "is movable!")
        
        moveSingleHorseWithColorRule(horseNum, horseDirs, horsePoses, horseOnAnother, horseLayers, horseGraph)
        # print("-- moved! --")
        # printState(horsePoses, horseOnAnother, horseLayers)
        
def existsHeightLargerThan(horseLayers, height):
    for layer in horseLayers:
        if len(layer) + 1 >= height:
            return True
    return False

time = 0
while True:
    if time > 1000:
        time = -1
        break
    if existsHeightLargerThan(horseLayers, 4):
        print(horseLayers)
        print("got it!")
        break
    
    for horseNum in range(1, K + 1):
        moveSingleHorseWithColorRule(horseNum, horseDirs, horsePoses, horseOnAnother, horseLayers, horseGraph)
    time += 1

print(time)
