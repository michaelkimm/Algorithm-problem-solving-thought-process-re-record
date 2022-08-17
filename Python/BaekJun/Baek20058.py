import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N, Q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(2**N)]

LevelList = list(map(int, input().split()))

def getLRReverseArray(array):
    return list(array[i][::-1] for i in range(len(array)))

def get2DTranspose(array):
    return list(map(list, zip(*array)))

def getCW2DArray(array):
    return getLRReverseArray(get2DTranspose(array))

def rotatePartial2DArray(graph, si, sj, L):
    temp2DArray = [graph[i][sj:sj+2**L] for i in range(si, si+2**L)]
    cw2DArray = getCW2DArray(temp2DArray)

    # graph에 적용
    for i in range(si, si + 2**L):
        for j in range(sj, sj + 2**L):
            graph[i][j] = cw2DArray[i - si][j - sj]

def rotateWith2LRule(graph, L):
    global N
    if L == 0:
        return
    # 부분 2차원 배열 시작 인덱스 구하기
    startIdx = []
    for i in range(0, 2**N, 2**L):
        for j in range(0, 2**N, 2**L):
            startIdx.append((i, j))
    
    # 부분 2차원 배열 시작 인덱스와 L로 각 부분 2차원 배열 회전하기
    for i, j in startIdx:
        rotatePartial2DArray(graph, i, j, L)

def getAdjacentIceCnt(graph, i, j):
    global N, di, dj
    cnt = 0
    
    for idx in range(4):
        ni = i + di[idx]
        nj = j + dj[idx]
        # 인접 칸의 인덱스가 나간 경우
        if not(0 <= ni < 2**N and 0 <= nj < 2**N):
            continue
        # 인접 칸이 0인 경우
        if graph[ni][nj] != 0:
            cnt += 1

    return cnt

def startMelting(graph):
    global N
    meltNeedList = []
    for i in range(2**N):
        for j in range(2**N):
            if graph[i][j] <= 0:
                continue
            adjacentIceCnt = getAdjacentIceCnt(graph, i, j)
            if not (adjacentIceCnt >= 3):
                meltNeedList.append((i, j))

    for i, j in meltNeedList:
        graph[i][j] -= 1

def doFireStorm(graph, L):
    rotateWith2LRule(graph, L)
    startMelting(graph)

def getIceLefts(graph):
    global N
    total = 0
    for i in range(2**N):
        for j in range(2**N):
            total += graph[i][j]

    return total

def getBiggestGroupSizeByDfs(graph):
    global N, di, dj
    visited = set([])
    maxSize = 0
    for i in range(2**N):
        for j in range(2**N):
            start = (i, j)
            if graph[i][j] == 0:
                continue
            if start in visited:
                continue
            stack = [start]
            visited.add(start)
            size = 0
            while stack:
                ci, cj = stack.pop()
                size += 1
                maxSize = max(size, maxSize)

                for idx in range(4):
                    ni = ci + di[idx]
                    nj = cj + dj[idx]
                    if not(0 <= ni < 2**N and 0 <= nj < 2**N):
                        continue
                    if graph[ni][nj] == 0:
                        continue
                    if (ni, nj) in visited:
                        continue
                    visited.add((ni, nj))
                    stack.append((ni, nj))
    return maxSize


for L in LevelList:
    doFireStorm(graph, L)

print(getIceLefts(graph))
print(getBiggestGroupSizeByDfs(graph))