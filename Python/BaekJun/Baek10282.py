import heapq
import sys
input = sys.stdin.readline

INF = int(1e10)

def dijkstra(start, graph):
    dist = [INF for _ in range(len(graph))]
    dist[start] = 0
    startNode = (0, start)
    hp = [startNode]
    while hp:
        cost, curNode = heapq.heappop(hp)
        if cost > dist[curNode]:
            continue
        for v, c in graph[curNode]:
            newCost = cost + c
            if newCost < dist[v]:
                heapq.heappush(hp, (newCost, v))
                dist[v] = newCost
    
    timeConsumed = 0
    computerCnt = 0
    for computer in range(1, len(graph)):
        if dist[computer] == INF:
            continue
        computerCnt += 1
        timeConsumed = max(timeConsumed, dist[computer])
    
    return computerCnt, timeConsumed

answers = []
n = int(input())
for _ in range(n):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int ,input().split())
        graph[b].append((a, s))
    result = dijkstra(c, graph)
    answers.append(result)
    
for cnt, time in answers:
    print(cnt, time)
    