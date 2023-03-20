from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def copy2DArray(ary):
    return [[ary[i][j] for j in range(len(ary[0]))] for i in range(len(ary))]

def spreadVirus(graph, visited):
    N = len(graph)
    M = len(graph[0])
    
    visited[i][j] = True
    start = (i, j)
    q = deque([start])
    while q:
        ci, cj = q.popleft()
        for dirIdx in range(4):
            ni = ci + di[dirIdx]
            nj = cj + dj[dirIdx]
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if visited[ni][nj]:
                continue
            if graph[ni][nj] == 1:
                continue
            graph[ni][nj] = 2
            visited[ni][nj] = True
            q.append((ni, nj))
            
    

def findMaxSecureAreaSize(graph):
    maxSecureAreaSize = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0:
                maxSecureAreaSize += 1
    return maxSecureAreaSize

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

initialWallPoses = set()
initialVirusPoses = set()
emptyPoses = set()
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 1:
            initialWallPoses.add((i, j))
        elif graph[i][j] == 2:
            initialVirusPoses.add((i, j))
        else:
            emptyPoses.add((i, j))
wallCases = list(combinations(emptyPoses, 3))

answer = 0
for w1, w2, w3 in wallCases:
    newGraph = copy2DArray(graph)
    newGraph[w1[0]][w1[1]] = 1
    newGraph[w2[0]][w2[1]] = 1
    newGraph[w3[0]][w3[1]] = 1
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i, j in initialVirusPoses:
        if visited[i][j]:
            continue
        spreadVirus(newGraph, visited)
    tmpResult = findMaxSecureAreaSize(newGraph)
    answer = max(tmpResult, answer)

print(answer)