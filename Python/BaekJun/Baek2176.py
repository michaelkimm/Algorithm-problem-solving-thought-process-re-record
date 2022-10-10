from collections import deque
import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))
S = 1
T = 2

def dijkstra(graph, start, end):
    N = len(graph) - 1
    dist = 0
    distance = [int(1e10) for _ in range(N  + 1)]
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
    return distance

def bfs(graph, distance):
    global S, T
    ret = 0
    # 현재 노드 위치
    q = deque([S])
    while q:
        curNum = q.popleft()
        if curNum == T:
            ret += 1
            continue
        for nextNum, cost in graph[curNum]:
            if distance[curNum] <= distance[nextNum]:
                continue
            q.append(nextNum)
    return ret

distance = dijkstra(graph, T, S)
answer = bfs(graph, distance)
print(answer)