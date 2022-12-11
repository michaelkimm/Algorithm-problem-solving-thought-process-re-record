import sys
input = sys.stdin.readline

N = int(input().strip())
graph = []
for _ in range(N):
    graph.append(list(input().strip()))

for i in range(N):
    for j in range(N):
        if graph[i][j] == '#':
            graph[i][j] = -1
        else:
            graph[i][j] = int(graph[i][j])

# 12시부터 시계방향
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

answer = 0
for ci in range(1, N - 1):
    for cj in range(1, N - 1):
        if ci >= 2 and cj >= 2 and ci <= N - 3 and cj <= N - 3:
            answer += 1
            continue

        zeroExist = False
        for dirIdx in range(8):
            ni = ci + di[dirIdx]
            nj = cj + dj[dirIdx]
            if graph[ni][nj] == -1:
                continue
            elif graph[ni][nj] == 0:
                zeroExist = True
                break
        if not zeroExist:
            answer += 1
            for dirIdx in range(8):
                ni = ci + di[dirIdx]
                nj = cj + dj[dirIdx]
                if graph[ni][nj] == -1:
                    continue
                else:
                    graph[ni][nj] -= 1

print(answer)