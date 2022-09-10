import heapq
import sys
input = sys.stdin.readline 

N, P, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(P):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))
cost = 0
startNode = 1
distance = [int(1e10)] * (N + 1)
linkedBeforeLineWeight = [0] * (N + 1)
nearest = [i for i in range(N + 1)]
distance[startNode] = 0
path = [0] * (K + 1)
hp = [(cost, startNode, path)]
arrivable = False
while hp:
    dist, curNode, path = heapq.heappop(hp)
    # if dist > distance[curNode]:
        # continue
    if curNode == N:
        arrivable = True
        break
    for v, cost in graph[curNode]:
        newDist = max(dist, cost)
        newPath = [val for val in path]
        newPath[-1] = newDist
        newPath.sort(reverse=True)
        if newPath[K] >
        if newDist < distance[v]:
            distance[v] = newDist
            heapq.heappush(hp, (newDist, v))
            linkedBeforeLineWeight[v] = newDist
            nearest[v] = curNode


print("nearest:", nearest)

if arrivable:
    linkedBeforeLineWeight.sort(reverse=True)
    # print("linkedBeforeLineWeight:", linkedBeforeLineWeight)
    print(linkedBeforeLineWeight[K])
else:
    print(-1)