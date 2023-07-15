import heapq
import sys
input = sys.stdin.readline

INF = 2000000001

N, M, A, B, C = map(int, input().split())
inputs = [list() for _ in range(M)]
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))
answer = INF
visited = [False for _ in range(N + 1)]


def dfs(start, end, maxCost, totalCost):
    global answer, C
    if start == end:
        if totalCost <= C:
            answer = min(answer, maxCost)
        return
    
    for v, c in graph[start]:
        if visited[v]:
            continue

        visited[v] = True
        dfs(v, end , max(maxCost, c), totalCost + c)
        visited[v] = False

def dfs(start, end):
    global answer, C
    stack = [(start, 0, 0)] # start, maxCost, totalCost
    visited[start] = True
    while stack:
        curNode, maxCost, totalCost = stack.pop()
        # print("curNode:", curNode, "\tmaxCost:", maxCost, "\ttotalCost:", totalCost)

        if curNode == end:
            if totalCost <= C:
                answer = min(answer, maxCost)
            visited[end] = False
            continue
    
        for v, c in graph[curNode]:
            if visited[v]:
                continue

            visited[v] = True
            stack.append((v, max(maxCost, c), totalCost + c))


def dij():
    global N, M, A, B, C, answer
    distance = [INF for _ in range(N + 1)]
    hp = [(0, 0, A)] # 초ㅣ대 수치심, totalCost, 노드
    while hp:
        maxCost, totalCost, curNode = heapq.heappop(hp)
        if curNode == B:
            answer = min(answer, maxCost)
            return
        if distance[curNode] < maxCost:
            continue
        for v, c in graph[curNode]:
            newMaxCost = max(maxCost, c)
            newTotalCost = totalCost + c
            if newMaxCost > distance[v] or newTotalCost > C:
                continue
            distance[v] = newMaxCost
            heapq.heappush(hp, (newMaxCost, newTotalCost, v))

dfs(A, B)

if answer == INF:
    print(-1)
else:
    print(answer)