N, M = map(int, input().split())
board = []

for _ in range(N):
    board = list(input().split())

# 위치 초기화
redPos  = [0, 0]
bluePos  = [0, 0]
targetPos  = [0, 0]

# 빨간 공 찾기 & 파란 공 찾기 & 도착 지점 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            redPos = [i, j]
        elif board[i][j] == 'B':
            bluePos = [i, j]
        elif board[i][j] == 'O':
            targetPos = [i, j]

#