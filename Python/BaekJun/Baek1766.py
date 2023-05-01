import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
inDegree = [0 for _ in range(N + 1)]
hp = []
visited = set()
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    inDegree[v] += 1

for i in range(1, N + 1):
    if inDegree[i] == 0:
        visited.add(i)
        heapq.heappush(hp, i)

answer = []
while hp:
    curNode = heapq.heappop(hp)
    answer.append(curNode)
    for v in graph[curNode]:
        if v in visited:
            continue
        inDegree[v] -= 1
        if inDegree[v] == 0:
            visited.add(v)
            heapq.heappush(hp, v)

print(' '.join(map(str, answer)))