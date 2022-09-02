import math
import heapq
from itertools import combinations
from collections import defaultdict
import sys
input = sys.stdin.readline

sx, sy, ex, ey = map(int, input().split())
N = int(input())
# warn : 중복 확인 필요
villages = [tuple(map(int, input().split())) for _ in range(N)]

def getLengthInInt(u, v):
    ux, uy = u
    vx, vy = v
    return int(math.sqrt(math.pow(ux - vx, 2) + math.pow(uy - vy, 2)))

def getPrimeNumberCheckListLowerThan(maxNum):
    isPrimeNumber = [False, False] + [True] * (maxNum - 1)
    for num in range(2, maxNum + 1):
        if isPrimeNumber[num]:
            for multipliedNum in range(num * 2, maxNum + 1, num):
                isPrimeNumber[multipliedNum] = False
    return isPrimeNumber

def dijkstra(startIdx, endIdx, graph, primeNumberCheckList):
    INF = int(1e10)
    distance = [INF] * len(graph)
    
    hp = [(0, startIdx)]
    distance[startIdx] = 0

    while hp:
        dist, curIdx = heapq.heappop(hp)
        curPt = graph[curIdx]
        if distance[curIdx] < dist:
            continue

        for nextIdx, nextPt in enumerate(graph):
            lineLength = getLengthInInt(curPt, nextPt)
            if not primeNumberCheckList[lineLength]:
                continue
            cost = dist + lineLength
            if cost < distance[nextIdx]:
                distance[nextIdx] = cost
                heapq.heappush(hp, (cost, nextIdx))

    if distance[endIdx] == INF or distance[endIdx] == 0:
        return -1
    else:
        return distance[endIdx]

villages.append((sx, sy))
villages.append((ex, ey))
villages = list(set(villages))
startIdx = villages.index((sx, sy))
endIdx = villages.index((ex, ey))

primeNumberCheckList = getPrimeNumberCheckListLowerThan(15000)
answer = dijkstra(startIdx, endIdx, villages, primeNumberCheckList)

print(answer)