from collections import deque
import sys
input = sys.stdin.readline

def print2DArray(array):
    print("=================")
    for line in array:
        print(line)

# 동남서북
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())
K = int(input())
applePoses = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
movementDict = dict()
for time, spinDir in list(list(input().split()) for _ in range(L)):
    movementDict[int(time)] = spinDir

graph = [['.' for _ in range(N)] for _ in range(N)]
graph[0][0] = 's'
for i, j in applePoses:
    graph[i - 1][j - 1] = 'a'

def rotate(curDir, spinDir):
    if spinDir == 'L':
        curDir = (curDir + 3) % 4
    elif spinDir == 'D':
        curDir = (curDir + 1) % 4
    return curDir

def goFront(graph, snakePoses, curDir):
    ni = snakePoses[0][0] + di[curDir]
    nj = snakePoses[0][1] + dj[curDir]
    if not (0 <= ni < len(graph) and 0 <= nj < len(graph[0])):
        return False
    if graph[ni][nj] == 's':
        return False

    snakePoses.appendleft((ni, nj))
    if graph[ni][nj] == 'a':
        graph[ni][nj] = 's'
    elif graph[ni][nj] == '.':
        graph[ni][nj] = 's'
        tailPose = snakePoses.pop()
        graph[tailPose[0]][tailPose[1]] = '.'

    return True

snakePoses = deque([(0, 0)])
curDir = 0
timePassed = 0
alive = True
while alive:
    timePassed += 1
    spinDir = 'G'
    alive = goFront(graph, snakePoses, curDir)
    if timePassed in movementDict:
        spinDir = movementDict[timePassed]
        curDir = rotate(curDir, spinDir)

print(timePassed)