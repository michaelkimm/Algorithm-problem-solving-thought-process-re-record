from itertools import permutations
import sys
input = sys.stdin.readline

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def print2DArray(array):
    print("=================")
    for line in array:
        print(line)

def moveLeft(graph):
    new = []
    N = len(graph)
    for i in range(N):
        prev = -1
        temp = []
        for j in range(N):
            if prev == -1 and graph[i][j] != 0:
                prev = graph[i][j]
            elif prev == -1 and graph[i][j] == 0:
                continue
            elif prev != -1 and prev == graph[i][j]:
                temp.append(2 * graph[i][j])
                prev = -1
            elif prev != -1 and prev != graph[i][j] and graph[i][j] != 0:
                temp.append(prev)
                prev = graph[i][j]
        if prev != -1:
            temp.append(prev)
        for _ in range(N - len(temp)):
            temp.append(0)
        new.append(temp)
    return new

def moveRight(graph):
    newGraph = [line[::-1] for line in graph]
    return [line[::-1] for line in moveLeft(newGraph)]

def moveUp(graph):
    newGraph = list(zip(*graph))
    return list(zip(*moveLeft(newGraph)))

def moveDown(graph):
    newGraph = list(zip(*graph))
    return list(zip(*moveRight(newGraph)))

def dfs(graph, neededMovementCnt):
    if neededMovementCnt == 0:
        return max(list(max(line) for line in graph))
    
    v1 = dfs(moveLeft(graph), neededMovementCnt - 1)
    v2 = dfs(moveRight(graph), neededMovementCnt - 1)
    v3 = dfs(moveDown(graph), neededMovementCnt - 1)
    v4 = dfs(moveUp(graph), neededMovementCnt - 1)

    return max(v1, v2, v3, v4)

# print(dfs(graph, 5))
graph = moveUp(graph)
print2DArray(graph)
graph = moveRight(graph)
print2DArray(graph)