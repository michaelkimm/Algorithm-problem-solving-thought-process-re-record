# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def print2DArray(ary):
    print("======")
    for line in ary:
        print(line)

def makeCustomWall(wall):
    customWall = []
    for ci, line in enumerate(wall):
        blockSizes = list(map(int, line.split()))
        blocks = []
        leftBlockCnt = 0
        for blockSize in blockSizes:
            for _ in range(blockSize):
                blocks.append((ci, leftBlockCnt))
            leftBlockCnt += 1
        customWall.append(blocks)
    return customWall

def getAdjacentWallCnt(wall, si, sj):
    criteriaBlockData = wall[si][sj]
    visited = set([])
    ci = si
    for cj in range(sj, len(wall[0])):
        if wall[ci][cj] != criteriaBlockData:
            break
        for dirIdx in range(4):
            ni = ci + di[dirIdx]
            nj = cj + dj[dirIdx]
            if not (0 <= ni < len(wall) and 0 <= nj < len(wall[0])):
                continue
            if wall[ni][nj] in visited:
                continue
            if (si, sj) == wall[ni][nj]:
                continue
            visited.add(wall[ni][nj])
    return len(visited)

def solution(wall):
    # if len(wall) <= 2:
        # return [[]]
    answer = []
    maxAdjacentBlockCnt = 0
    customWall = makeCustomWall(wall)
    visited = set([])
    for i in range(len(customWall)):
        for j in range(len(customWall[0])):
            if customWall[i][j] in visited:
                continue
            adjacentBlockCnt = getAdjacentWallCnt(customWall, i, j)
            visited.add(customWall[i][j])

            if adjacentBlockCnt > maxAdjacentBlockCnt:
                answer = []
                answer.append([customWall[i][j][0], customWall[i][j][1]])
                maxAdjacentBlockCnt = adjacentBlockCnt
            elif adjacentBlockCnt == maxAdjacentBlockCnt:
                answer.append([customWall[i][j][0], customWall[i][j][1]])

    answer.sort()
    return answer