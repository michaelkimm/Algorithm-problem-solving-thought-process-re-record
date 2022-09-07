import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))

start, end = map(int, input().split())

distance = [1e12] * (n + 1)
distance[start] = 0
hp = [(0, start)]
before = [i for i in range(n + 1)]

while hp:
    dist, curNum = heapq.heappop(hp)
    if dist > distance[curNum]:
        continue

    for v, cost in graph[curNum]:
        newDist = dist + cost
        if newDist < distance[v]:
            distance[v] = newDist
            heapq.heappush(hp, (newDist, v))
            before[v] = curNum

def setRetPassed(before, end, retPassedList):
    retPassedList.append(end)
    if before[end] == end:
        return
    setRetPassed(before, before[end], retPassedList)

retPassedList = []
setRetPassed(before, end, retPassedList)
retPassedList.reverse()


print(distance[end])
print(len(retPassedList))
for num in retPassedList:
    print(num, end=' ')