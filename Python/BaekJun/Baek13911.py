import heapq
import sys
input = sys.stdin.readline
INF = int(1e10)

def dijkstra(startNums, V, graph, k):
    distance = [INF] * (V + 1)
    hp = []
    for num in startNums:
        heapq.heappush(hp, (0, num))
        distance[num] = 0
    
    while hp:
        dist, curNum = heapq.heappop(hp)
        if distance[curNum] < dist:
            continue
        for v, cost in graph[curNum]:
            newCost = dist + cost
            if newCost < distance[v] and newCost <= k:
                distance[v] = newCost
                heapq.heappush(hp, (newCost, v))

    return distance

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

M, x = map(int, input().split())
macdoNums = list(map(int, input().split()))
S, y = map(int, input().split())
starNums = list(map(int, input().split()))

macdoToNums = dijkstra(macdoNums, V, graph, x)
starToNums = dijkstra(starNums, V, graph, y)

answer = INF
for num in range(1, V + 1):
    # macdoToNums[num] == 0이면 맥도날드가 있으므로 제외, == INF면 조건 만족하지 않는 곳이라 제외
    if not (0 < macdoToNums[num] < INF and 0 < starToNums[num] < INF):
        continue
    answer = min(answer, macdoToNums[num] + starToNums[num])

print(answer if answer != INF else -1)