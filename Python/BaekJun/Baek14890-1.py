import sys
input = sys.stdin.readline

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


availLine = [3, 2, 2, 1, 1, 1]
unavailLine = [3, 3, 3, 2, 1, 2]

def canMakeUpBridge(line, i, bridgeExists, L, consecCnt):
    if i - (L - 1) < 0 or consecCnt < L:
        return False

    result = True
    for j in range(i, i - L, -1):
        if bridgeExists[j]:
            result = False
            break
        bridgeExists[j] = True
    return result

def canMakeDownBridge(line, i, bridgeExists, L):
    if i + L - 1 >= len(line):
        return False

    result = True
    for j in range(i, i + L):
        if line[j] != line[i] or bridgeExists[j]:
            result = False
            break
        bridgeExists[j] = True
    return result

def checkPassable(line, L):
    result = True
    prev = line[0]
    consecCnt = 1
    bridgeExists = [False for _ in range(len(line))]
    for i in range(1, len(line)):
        if line[i] == (prev - 1):
            if canMakeDownBridge(line, i, bridgeExists, L):
                for j in range(L):
                    bridgeExists[i+j] = True
                prev = line[i]
                consecCnt = 1
            else:
                result = False
                break
        elif line[i] == prev:
            prev = line[i]
            consecCnt += 1
            continue
        elif line[i] == (prev + 1):
            if canMakeUpBridge(line, i - 1, bridgeExists, L, consecCnt):
                for j in range(i - 1, i - 1 - L, -1):
                    bridgeExists[j] = True
                prev = line[i]
                consecCnt = 1
            else:
                result = False
                break
        else:
            result =False
            break
    return result

answer = 0
for i in range(len(graph)):
    if checkPassable(graph[i][:], L):
        answer += 1

graph = list(zip(*graph))
for i in range(len(graph)):
    if checkPassable(graph[i][:], L):
        answer += 1

print(answer)