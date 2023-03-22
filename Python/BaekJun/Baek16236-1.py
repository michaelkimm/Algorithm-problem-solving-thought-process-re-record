from collections import deque
from collections import defaultdict
import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def getPose(graph, value):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == value:
                return i, j
    return -1, -1

def print2DArray(ary):
    print("=================")
    for line in ary:
        print(line)

def getEatableFishes(graph, babySharkPose, sharkSize):
    eatableFishes = []
    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
    dist = 0
    start  = (dist, babySharkPose[0], babySharkPose[1])
    visited[babySharkPose[0]][babySharkPose[1]] = True
    q = deque([start])
    while q:
        dist, si, sj = q.popleft()

        for dirIdx in range(4):
            ni = si + di[dirIdx]
            nj = sj + dj[dirIdx]
            if not (0 <= ni < len(graph) and 0 <= nj < len(graph[0])):
                continue
            if visited[ni][nj]:
                continue
            if graph[ni][nj] > sharkSize:
                continue
            if graph[ni][nj] < sharkSize and graph[ni][nj] != 0:
                eatableFishes.append((dist + 1, ni, nj, graph[ni][nj]))
                visited[ni][nj] = True
                continue
            visited[ni][nj] = True
            q.append((dist + 1, ni, nj))
    return eatableFishes

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

babySharkPose = getPose(graph, 9)
sharkSize = 2
eatenCnt = 0
timePassed = 0

# print(getEatableFishes(graph, babySharkPose, sharkSize))
eatableFishes = getEatableFishes(graph, babySharkPose, sharkSize)
while eatableFishes:
    eatableFishes.sort()
    if eatableFishes:
        dist, fi, fj, size = eatableFishes[0]
        timePassed += dist
        graph[babySharkPose[0]][babySharkPose[1]] = 0
        babySharkPose = (fi, fj)
        eatenCnt += 1
        graph[fi][fj] = 9
        if eatenCnt >= sharkSize:
            sharkSize += 1
            eatenCnt = 0
    eatableFishes = getEatableFishes(graph, babySharkPose, sharkSize)
print(timePassed)