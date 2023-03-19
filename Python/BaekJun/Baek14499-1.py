import sys
input = sys.stdin.readline

# 동쪽은 0, 서쪽은 1, 북쪽은 2, 남쪽은 3
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

N, M, ci, cj, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
movements = [v - 1 for v in list(map(int, input().split()))]

# 윗면, 아래면, 좌측면, 우측면, 앞면, 뒷면
dice = [0, 0, 0, 0, 0, 0]
def moveDice(dice, direction):
    if direction == 0:
        dice = [dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]]
    elif direction == 1:
        dice = [dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]]
    elif direction == 2:
        dice = [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]
    elif direction == 3:
        dice = [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
    return dice
    
def copyNumbersBetweenDiceAndGraph(graph, dice, ci, cj):
    if graph[ci][cj] == 0:
        graph[ci][cj] = dice[1]
    else:
        dice[1] = graph[ci][cj]
        graph[ci][cj] = 0

def executeMoveStatement(graph, dice, ci, cj, moveDir):
    ni = ci + di[moveDir]
    nj = cj + dj[moveDir]
    if not (0 <= ni < len(graph) and 0 <= nj < len(graph[0])):
        return ci, cj, dice

    dice = moveDice(dice, moveDir)
    copyNumbersBetweenDiceAndGraph(graph, dice, ni, nj)
    print(dice[0])

    return ni, nj, dice

for movement in movements:
    ci, cj, dice = executeMoveStatement(graph, dice, ci, cj, movement)