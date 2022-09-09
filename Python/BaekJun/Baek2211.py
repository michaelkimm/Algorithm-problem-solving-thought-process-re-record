import heapq
import sys
input = sys.stdin.readline

def getMinNeededGraphLineSingle(beforeVisited, N, num):
    ret = []
    while beforeVisited[num] != num:
        ret.append((min(num, beforeVisited[num]), max(num, beforeVisited[num])))
        num = beforeVisited[num]
    return ret

def getMinNeededGraphLineAll(beforeVisited, N):
    ret = []
    for num in range(1, N + 1):
        result = getMinNeededGraphLineSingle(beforeVisited, N, num)
        ret += result
    return set(ret)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))

startNode = 1
dist = 0
distance = [int(1e10)] * (N + 1)
hp = [(dist, startNode)]
distance[startNode] = 0
beforeVisited = [i for i in range(N + 1)]

while hp:
    dist, curNode = heapq.heappop(hp)
    if distance[curNode] < dist:
        continue
    for v, cost in graph[curNode]:
        newCost = dist + cost
        if newCost < distance[v]:
            beforeVisited[v] = curNode
            distance[v] = newCost
            heapq.heappush(hp, (newCost, v))
    
minNeededGraphLine = getMinNeededGraphLineAll(beforeVisited, N)
print(len(minNeededGraphLine))
for u, v in minNeededGraphLine:
    print(u, v)