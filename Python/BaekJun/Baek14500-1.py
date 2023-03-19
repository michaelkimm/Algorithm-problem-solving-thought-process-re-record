import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

oneDimTetrominos = [[1, 1, 1, 1]]
twoDimtetrominos = [
    [[1],
    [1],
    [1],
    [1]],
    
    [[1, 1],
     [1, 1]],

    [[1, 0],
     [1, 0],
     [1, 1]],
    [[1, 1, 1],
     [1, 0, 0]],
    [[1, 1],
     [0, 1],
     [0, 1]],
    [[0, 0, 1],
     [1, 1, 1]],
    
    [[0, 1],
     [0, 1],
     [1, 1]],
    [[1, 0, 0],
     [1, 1, 1]],
    [[1, 1],
     [1, 0],
     [1, 0]],
    [[1, 1, 1],
     [0, 0, 1]],

    [[1, 0],
     [1, 1],
     [0, 1]],
    [[0, 1, 1],
     [1, 1, 0]],
    [[0, 1],
     [1, 1],
     [1, 0]],
    [[1, 1, 0],
     [0, 1, 1]],

    [[1, 1, 1],
     [0, 1, 0]],
    [[0, 1],
     [1, 1],
     [0, 1]],
    [[0, 1, 0],
     [1, 1, 1]],
    [[1, 0],
     [1, 1],
     [1, 0]],
]

def checkIfTetInAvailableRange(graph, tet, i, j):
    return (i + len(tet) - 1) < len(graph) and (j + len(tet[0]) - 1) < len(graph[0])

def sum2DArrays(ary1, ary2):
    result = 0
    for i in range(len(ary1)):
        for j in range(len(ary1[0])):
            result += (ary1[i][j] * ary2[i][j])
    return result

def getMaxTetSum(graph, tet):
    result = 0
    N = len(graph)
    M = len(graph[0])
    n = len(tet)
    m = len(tet[0])
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if not checkIfTetInAvailableRange(graph, tet, i, j):
                continue 
            smallGraph = [graph[ci][j:j+m] for ci in range(i, i+n)]
            result = max(result, sum2DArrays(smallGraph, tet))
    return result

answer = 0

for tet in twoDimtetrominos:
    answer = max(getMaxTetSum(graph, tet), answer)

for i in range(len(graph)):
    for j in range(len(graph[0]) - 3):
        answer = max(answer, sum(graph[i][j:j+4]))

print(answer)