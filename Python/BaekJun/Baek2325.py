import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))


def getShortestPath(graph):
    N = len(graph) - 1
    start = 1
    end = N
    dist = 0
    distance = [int(1e10) for _ in range(N + 1)]
    before = [i for i in range(N + 1)]
    distance[start] = 0
    hp = [(dist, start)]
    while hp:
        dist, curNum = heapq.heappop(hp)
        if distance[curNum] < dist:
            continue
        for nextNum, cost in graph[curNum]:
            newDist = dist + cost
            if newDist < distance[nextNum]:
                distance[nextNum] = newDist
                heapq.heappush(hp, (newDist, nextNum))
                before[nextNum] = curNum
    return before


def dijkstra(graph, u, v):
    N = len(graph) - 1
    start = 1
    end = N
    dist = 0
    distance = [int(1e10) for _ in range(N  + 1)]
    distance[start] = 0
    hp = [(dist, start)]
    while hp:
        dist, curNum = heapq.heappop(hp)
        if distance[curNum] < dist:
            continue
        for nextNum, cost in graph[curNum]:
            if (curNum == u and nextNum == v) or (curNum == v and nextNum == u):
                continue
            newDist = dist + cost
            if newDist < distance[nextNum]:
                distance[nextNum] = newDist
                heapq.heappush(hp, (newDist, nextNum))
    return distance[N]

path = getShortestPath(graph)
answer = 0
for n1, n2 in enumerate(path):
    if n1 == 0: continue
    result = dijkstra(graph, n1, n2)
    answer = max(answer, result)

print(answer)