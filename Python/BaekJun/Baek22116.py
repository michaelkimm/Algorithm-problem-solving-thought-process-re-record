import heapq
import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]
INF = int(1e10)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

distance = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
distance[0][0] = 0
startNode = (0, 0, 0)
hp = [startNode]
answer = 0
while hp:
    dist, ci, cj = heapq.heappop(hp)
    if dist > distance[ci][cj]:
        continue

    if ci == N - 1 and cj == N - 1:
        answer = dist
        break
    
    for dirIdx in range(4):
        ni = ci + di[dirIdx]
        nj = cj + dj[dirIdx]
        if not (0 <= ni < N and 0 <= nj < N):
            continue
        dHeight = abs(graph[ci][cj] - graph[ni][nj])
        newCost = max(dist, dHeight)
        if newCost < distance[ni][nj]:
            distance[ni][nj] = newCost
            heapq.heappush(hp, (newCost, ni, nj))

print(answer)