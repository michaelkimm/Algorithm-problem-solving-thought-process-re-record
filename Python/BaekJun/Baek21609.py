from collections import deque
import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 검은색 블록은 -1, 무지개 블록은 0, 빈칸은 -2

class BlockGroup:
    def __init__(self, blockPose, blockColor):
        self.blocks = [blockPose]
        self.standard = (0, 0)
        self.normalBlockCnt = 1
        self.blockColor = blockColor

    def addBlock(self, blockPose, isNormalBlock):
        self.blocks.append(blockPose)
        if isNormalBlock:
            self.normalBlockCnt += 1
    
    def isBlockColorSame(self, blockColor):
        return self.blockColor == blockColor

    def autoSetStandardBlock(self, graph):
        temp = []
        for bi, bj in self.blocks:
            if graph[bi][bj] != 0:
                temp.append((bi, bj))
        temp.sort()
        self.standard = temp[0]

    def getBlockSize(self):
        return len(self.blocks)

    def getRainbowBlockCnt(self):
        return self.getBlockSize() - self.normalBlockCnt


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def isNormalBlock(blockColor):
    global M
    return 1 <= blockColor <= M

def bfs(si, sj, targetGraph):
    global N, M, di, dj
    if targetGraph[si][sj] <= 0:
        return -1

    visited = set()
    graph = targetGraph
    blockGroup = BlockGroup((si, sj), graph[si][sj])
    visited.add((si, sj))
    q = deque([(si, sj)])

    while q:
        ci, cj = q.popleft()

        for idx in range(4):
            ni = ci + di[idx]
            nj = cj + dj[idx]
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if graph[ni][nj] <= -1:
                continue
            if isNormalBlock(graph[ni][nj]) and not blockGroup.isBlockColorSame(graph[ni][nj]):
                continue
            if (ni, nj) in visited:
                continue

            visited.add((ni, nj))
            blockGroup.addBlock((ni, nj), isNormalBlock(graph[ni][nj]))
            q.append((ni, nj))

    blockGroup.autoSetStandardBlock(graph)
    if blockGroup.getBlockSize() < 2:
        return -1
    return blockGroup

def getNextEraseBlockGroup(graph):
    global N, M
    blockGroups = []
    for i in range(N):
        for j in range(N):
            result = bfs(i, j, graph)
            if result == -1:
                continue
            blockGroups.append(result)
    
    if len(blockGroups) == 0:
        return -1

    blockGroups.sort(key=lambda bg:(-bg.getBlockSize(), -bg.getRainbowBlockCnt(), -bg.standard[0], -bg.standard[1]))
    return blockGroups[0]

def getScore(blockGroups):
    return len(blockGroups.blocks)**2

def eraseBlocks(blockGroups, graph):
    for i, j in blockGroups.blocks:
        graph[i][j] = -2
    return getScore(blockGroups)

def applyPartialGravity(bottomPose, curPose, q, j, graph):
    for i in range(bottomPose[0] - 1, curPose[0], -1):
        color = q.popleft() if len(q) >= 1 else -2
        graph[i][j] = color       

def applyGravity(graph):
    global N
    for j in range(N):
        q = deque([])
        bottomPose = (N, j)
        # 중력 받을 객체 선정
        for i in range(N - 1, -1 , -1):
            if graph[i][j] == -1:
                # 부분 중력 적용
                for pi in range(bottomPose[0] - 1, i, -1):
                    graph[pi][j] = q.popleft() if q else -2

                # 바닥 업데이트
                bottomPose = (i, j)
                continue
            if graph[i][j] == -2:
                continue
            q.append(graph[i][j])
        if q:
            for i in range(bottomPose[0] - 1, -1, -1):
                graph[i][j] = q.popleft() if q else -2

def flipHorizontally(graph):
    return [graph[i][::-1] for i in range(len(graph))]

def transepose(graph):
    return list(map(list, zip(*graph)))

def rotateCCW(graph):
    return transepose(flipHorizontally(graph))

blockGroups = getNextEraseBlockGroup(graph)
while blockGroups != -1:

    answer += eraseBlocks(blockGroups, graph)

    applyGravity(graph)

    graph = rotateCCW(graph)

    applyGravity(graph)

    blockGroups = getNextEraseBlockGroup(graph)

print(answer)