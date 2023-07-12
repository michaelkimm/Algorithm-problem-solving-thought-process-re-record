from collections import deque
import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

board = [list(input().strip()) for _ in range(5)]
picked = [[False for _ in range(5)] for _ in range(5)]
answer = 0

def checkAdjacent(picked, si, sj):
    visited = set([(si, sj)])
    q = deque([(si, sj)])
    totalCnt = 1 if picked[si][sj] else 0
    while q:
        ci, cj = q.popleft()
        for dirIdx in range(4):
            ni, nj = ci + di[dirIdx], cj + dj[dirIdx]
            if not (0 <= ni < 5 and 0 <= nj < 5):
                continue
            if not picked[ni][nj] or (ni, nj) in visited:
                continue
            visited.add((ni, nj))
            q.append((ni, nj))
            totalCnt += 1

    return True if totalCnt == 7 else False


def recursive(cIdx, sCnt, yCnt):
    global answer, board, picked
    if (sCnt + yCnt) == 7:
        cIdx -= 1
        ci, cj = cIdx // 5, cIdx % 5
        if sCnt > yCnt and checkAdjacent(picked, ci, cj):
            answer += 1
        return
    
    for idx in range(cIdx, 25):
        i, j = idx // 5, idx % 5
        picked[i][j] = True

        nSCnt = sCnt + 1 if board[i][j] == 'S' else sCnt
        nYCnt = yCnt + 1 if board[i][j] == 'Y' else yCnt

        recursive(idx + 1, nSCnt, nYCnt)
        picked[i][j] = False

recursive(0, 0, 0)
print(answer)

