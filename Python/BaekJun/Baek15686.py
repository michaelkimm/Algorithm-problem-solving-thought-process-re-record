from itertools import combinations
import sys
import math
input = sys.stdin.readline

def getDist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

def getCityChickenDist(houses, chickenMarkets):
    ret = 0
    for house in houses:
        minDist = int(1e10)
        for market in chickenMarkets:
            minDist = min(minDist, getDist(house, market))
        ret += minDist
    return ret

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

houses = []
chickenMarket = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            chickenMarket.append((i, j))

pickCases = list(combinations(chickenMarket, M))
minCityChickenDist = int(1e10)
for case in pickCases:
    minCityChickenDist = min(minCityChickenDist, getCityChickenDist(houses, case))

print(minCityChickenDist)