import heapq
import sys
input = sys.stdin.readline

INF = int(1e10)

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))

start, end = map(int, input().split())

distances = [INF for _ in range(N + 1)]
start_node = (0, start) # cost, 노드 번호
distances[start] = 0
hp = [start_node]
while hp:
    dist, curNode = heapq.heappop(hp)
    if distances[curNode] < dist:
        continue
    for v, c in graph[curNode]:
        newDist = dist + c
        if newDist < distances[v]:
            distances[v] = newDist
            heapq.heappush(hp, (newDist, v))

print(distances[end])