import sys
input = sys.stdin.readline

# 0 = 시계 방향, 1 = 반시계 방향
# i번째 배열 회전
def rotate(queues, idx, dir):
    if dir == 0:
        val = queues[idx].pop()
        queues[idx].insert(0, val)
    else:
        val = queues[idx].pop(0)
        queues[idx].append(val)

def eraseAdjacent(queues):
    erasedReserved = set()
    for i in range(len(queues)):
        for j in range(len(queues[0])):
            if queues[i][j] == 0:
                continue
            if checkAdjacent(queues, i, j):
                erasedReserved.add((i, j))
    for i, j in erasedReserved:
        queues[i][j] = 0
    if erasedReserved:
        return True
    else:
        return False

def doBalancing(queues):
    N = len(queues)
    M = len(queues[0])
    numberLeftCnt = N * M - sum(q.count(0) for q in queues)
    if numberLeftCnt == 0:
        return
    averages = sum([sum(q) for q in queues]) / (numberLeftCnt)

    for i in range(N):
        for j in range(M):
            if queues[i][j] > averages:
                queues[i][j] -= 1
            elif 0 < queues[i][j] < averages:
                queues[i][j] += 1   

def checkAdjacent(queues, i, j):
    N = len(queues)
    M = len(queues[0])
    if j == 0:
        if queues[i][j] == queues[i][1] or queues[i][j] == queues[i][M - 1]:
            return True
    if j == M - 1:
        if queues[i][j] == queues[i][M - 2] or queues[i][j] == queues[i][0]:
            return True
    if 1 <= j <= M - 2:
        if queues[i][j] == queues[i][j - 1] or queues[i][j] == queues[i][j + 1]:
            return True
    if i == 0:
        if queues[i][j] == queues[i + 1][j]:
            return True
    if i == N - 1:
        if queues[i][j] == queues[N - 2][j]:
            return True
    if 1 <= i <= N - 2:
        if queues[i][j] == queues[i - 1][j] or queues[i][j] == queues[i + 1][j]:
            return True
    return False

N, M, T = map(int, input().split())
queues = []
for _ in range(N):
    queue = list(map(int, input().split()))
    queues.append(queue)

for _ in range(T):
    x, direction, times = list(map(int, input().split()))
    for i in range(x - 1, N, x):
        for _ in range(times):
            rotate(queues, i, direction)
    erased = eraseAdjacent(queues)
    if not erased:
        doBalancing(queues)
                    
result = sum(list(sum(q) for q in queues))
print(result)