import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

INF = int(1e10)

def dijkstra(keys, start, graphDict, n):
    global INF
    needToVisitFirst = dict()
    for key in keys:
        needToVisitFirst[key] = '-'
    # for node, c in graphDict[start]:
        # needToVisitFirst[node] = node

    distDict = dict()
    for key in keys:
        distDict[key] = INF
    
    startNode = (0, start)
    distDict[start] = 0
    hp = [startNode]
    while hp:
        dist, curNode = heapq.heappop(hp)
        if dist > distDict[curNode]:
            continue
        for v, c in graphDict[curNode]:
            newCost = dist + c
            if newCost < distDict[v]:
                distDict[v] = newCost
                heapq.heappush(hp, (newCost, v))
                if needToVisitFirst[curNode] == '-':
                    needToVisitFirst[v] = v
                else:
                    needToVisitFirst[v] = needToVisitFirst[curNode]

    for key in sorted(needToVisitFirst.keys()):
        print(needToVisitFirst[key], end = ' ')
    print()
    

n, m = map(int, input().split())
graphDict = defaultdict(list)
for _ in range(m):
    u, v, c = map(int, input().split())
    graphDict[u].append((v, c))
    graphDict[v].append((u, c))

for node in sorted(graphDict.keys()):
    dijkstra(graphDict.keys(), node, graphDict, n)
