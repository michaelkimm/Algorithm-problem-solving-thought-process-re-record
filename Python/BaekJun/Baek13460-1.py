from collections import deque
import heapq
import sys
input = sys.stdin.readline

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def findPose(graph, color):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == color:
                return i, j
    return -1, -1

def moveSingleBall(graph, ballPose, direction):
    ballColor = graph[ballPose[0]][ballPose[1]]
    while True:
        ni = ballPose[0] + di[direction]
        nj = ballPose[1] + dj[direction]
        if graph[ni][nj] == '#' or graph[ni][nj] == 'R' or graph[ni][nj] == 'B':
            break
        graph[ballPose[0]][ballPose[1]] = '.'
        ballPose = (ni, nj)
        if graph[ni][nj] == 'O':
            break
        graph[ballPose[0]][ballPose[1]] = ballColor

    return ballPose


# 상하좌우 구르기 구현
# 빨강과 파랑은 서로를 못지나감
def moveGraph(graph, direction, redPose, bluePose):
    # 그 뱡향 쪽에 더 가까운 애 먼저 전진
    if direction == 0:
        if redPose[0] < bluePose[0]:
            redPose = moveSingleBall(graph, redPose, direction)
            bluePose = moveSingleBall(graph, bluePose, direction)
        else:
            bluePose = moveSingleBall(graph, bluePose, direction)
            redPose = moveSingleBall(graph, redPose, direction)
    elif direction == 1:
        if redPose[0] > bluePose[0]:
            redPose = moveSingleBall(graph, redPose, direction)
            bluePose = moveSingleBall(graph, bluePose, direction)
        else:
            bluePose = moveSingleBall(graph, bluePose, direction)
            redPose = moveSingleBall(graph, redPose, direction)
    elif direction == 2:
        if redPose[1] < bluePose[1]:
            redPose = moveSingleBall(graph, redPose, direction)
            bluePose = moveSingleBall(graph, bluePose, direction)
        else:
            bluePose = moveSingleBall(graph, bluePose, direction)
            redPose = moveSingleBall(graph, redPose, direction)
    elif direction == 3:
        if redPose[1] > bluePose[1]:
            redPose = moveSingleBall(graph, redPose, direction)
            bluePose = moveSingleBall(graph, bluePose, direction)
        else:
            bluePose = moveSingleBall(graph, bluePose, direction)
            redPose = moveSingleBall(graph, redPose, direction)

    return (redPose, bluePose)

def clone2DArray(array):
    return [[array[i][j] for j in range(len(array[0]))] for i in range(len(array))]

def print2DArray(array):
    print("start ===============")
    for line in array:
        print(line)
    print("end ===============")

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]

redPose = findPose(graph, 'R')
bluePose = findPose(graph, 'B')
goalPose = findPose(graph, 'O')

answer = -1

initialGraph = clone2DArray(graph)
cost = 0
visitied = set((redPose, bluePose))
q = [(cost, initialGraph, redPose, bluePose)]

while q:
    cost, currentGraph, redPose, bluePose = heapq.heappop(q)
    if bluePose == goalPose:
        continue
    if redPose == goalPose:
        answer = cost
        break
    if cost >= 10:
        continue

    for dirIdx in range(4):
        newGraph = clone2DArray(currentGraph)
        newRedPose, newBluePose = moveGraph(newGraph, dirIdx, redPose, bluePose)
        if (newRedPose, newBluePose) in visitied:
            continue
        visitied.add((newRedPose, newBluePose))
        heapq.heappush(q, (cost + 1, newGraph, newRedPose, newBluePose))
        # q.append((cost + 1, newGraph, newRedPose, newBluePose))

if answer > 10:
    answer = -1

print(answer)