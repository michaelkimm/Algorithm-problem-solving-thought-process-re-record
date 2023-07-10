import sys
input = sys.stdin.readline

scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0, 13 ,16, 19, 25, 30, 35, 22, 24, 28, 27, 26]
graph = [[1], [2], [3], [4], [5], [6, 22], [7], [8], [9], [10], [11, 28], [12], [13], [14], [15], [16, 30], [17], [18], [19], [20], [21], [], [23], [24], [25], [26], [27], [20], [29], [25], [31], [32], [25]]


dice = list(map(int, input().split()))
answer = 0

def backTracking(loc, result, horces):
    global dice, scores, graph, answer
    if loc >= 10:
        answer = max(answer, result)
        return

    for i in range(4):
        x = horces[i]
        if x == 21:
            continue
        if len(graph[x]) == 2:
            x =  graph[x][1]
        else:
            x = graph[x][0]

        for _ in range(1, dice[loc]):
            if not graph[x]:
                break
            x = graph[x][0]

        if x == 21 or (x not in horces):
            before = horces[i]
            horces[i] = x
            backTracking(loc + 1, result + scores[x], horces)
            horces[i] = before


backTracking(0, 0, [0, 0, 0, 0])
print(answer)
