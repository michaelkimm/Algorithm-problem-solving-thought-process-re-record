import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ptMap = [list(map(int, input().split())) for _ in range(N)]

used = [[False for _ in range(M)] for _ in range(N)]
answer = 0

windows = [
    [[2, 1],
     [1, 0]],
    [[0, 1],
     [1, 2]],
    [[1, 0],
     [2, 1]],
    [[1, 2],
     [0, 1]]
]

def applicable(ci, cj, k, used):
    global windows, N, M
    for i in range(ci, ci + 2):
        for j in range(cj, cj + 2):
            if not (0 <= i < N and 0 <= j < M):
                return False
            if windows[k][i - ci][j - cj] == 0:
                continue
            else:
                if used[i][j]:
                    return False
    return True

def apply(ci, cj, k, used):
    global windows, ptMap
    result = 0
    for i in range(ci, ci + 2):
        for j in range(cj, cj + 2):
            if windows[k][i - ci][j - cj] == 0:
                continue
            used[i][j] = True
            result += (windows[k][i - ci][j - cj] * ptMap[i][j])
    return result

def detach(ci, cj, k, used):
    global windows
    for i in range(ci, ci + 2):
        for j in range(cj, cj + 2):
            if windows[k][i - ci][j - cj] == 0:
                continue
            used[i][j] = False

def recursive(startIdx, totalPts):
    global N, M, ptMap, used, answer
    if startIdx >= N * M:
        answer = max(answer, totalPts)
        return
    
    # 놓는 경우
    for idx in range(startIdx, N * M):
        i = idx // M
        j = idx % M
        for k in range(4):
            if not applicable(i, j, k, used):
                continue
            pts = apply(i, j, k, used)
            recursive(idx + 1, totalPts + pts)
            detach(i, j, k, used)

    # 안놓는 경우
    recursive(startIdx + 1, totalPts)
            
recursive(0, 0)
print(answer)
