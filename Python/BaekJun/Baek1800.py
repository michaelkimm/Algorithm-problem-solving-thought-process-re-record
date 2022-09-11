import heapq
import sys
input = sys.stdin.readline 

def duplicate2DArray(ary):
    ret = [[ary[i][j] for j in range(len(ary[i]))] for i in range(len(ary))]
    return ret

N, P, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(P):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))

cost = 0
startNode = 1
distance = [[] for _ in range(N + 1)]
distance[startNode].append([0] * (K + 1))
distance[startNode].sort(key=lambda x:x[K])
hp = [(cost, startNode)]
while hp:
    dist, curNode = heapq.heappop(hp)
    for v, cost in graph[curNode]:
        new2DArray = duplicate2DArray(distance[v])
        for i in range(len(new2DArray)):
            if new2DArray[i][K] < 