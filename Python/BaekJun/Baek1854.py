import heapq
import sys
input = sys.stdin.readline


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))


cost, curNode = 0, 1
INF = int(1e10)
distance = [[INF for _ in range(k)] for _ in range(n + 1)]
distance[curNode][k - 1] = cost
distance[curNode].sort()
hp = [(cost, curNode)]

while hp:
    dist, curNode = heapq.heappop(hp)
    if distance[curNode][k - 1] < dist:
        continue

    for v, cost in graph[curNode]:
        newDist = dist + cost

        if distance[v][k - 1] <= newDist:
            continue
        distance[v][k - 1] = newDist
        distance[v].sort()
        heapq.heappush(hp, (newDist, v))

for idx in range(1, n + 1):
    if distance[idx][k - 1] == INF:
        print(-1)
    else:
        print(distance[idx][k - 1])