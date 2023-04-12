import sys
input = sys.stdin.readline

# 서남동북
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

def print2DArray(graph):
    print("======")
    for line in graph:
        print(line)

def spreadTornado(graph, si, sj, moveDir):
    # left
    leftDir = (moveDir + 1) % 4
    # right
    rightDir = (moveDir -   1) % 4
    # front-left
    # front-right
    # back-lect
    # back-right

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


si, sj = N // 2, N // 2
graph[si][sj] = 0
curValue = 1
moveDir = 0
moveNeededCnt = 1

cnt = 0

while not (si == 0 and sj == 0):
    for _ in range(moveNeededCnt):
        ni = si + di[moveDir]
        nj = sj + dj[moveDir]
        if not (0 <= ni < N and 0 <= nj < N):
            continue
        # 여기에 바람 불기 함수 실행
        si, sj = ni, nj
        y = graph[si][sj]
        spreadTornado(graph, si, sj, moveDir)
        graph[si][sj] = curValue
        curValue += 1
    moveDir = (moveDir + 1) % 4
    if moveDir == 2 or moveDir == 0:
        moveNeededCnt += 1
    cnt += 1
    if cnt == 10:
        break

print2DArray(graph)