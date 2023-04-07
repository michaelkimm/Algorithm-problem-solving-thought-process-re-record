import heapq
import sys
input = sys.stdin.readline
INF = int(1e10)

def getMeetingSchedule(cameFrom, nodeNum):
    if cameFrom[nodeNum] == nodeNum:
        return [nodeNum]
    return getMeetingSchedule(cameFrom, cameFrom[nodeNum]) + [nodeNum]

T = int(input())
answer = []
for idx in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(M + 1)]
    for _ in range(N):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
        graph[v].append((u, c))
    start = 0
    end = M - 1
    distance = [INF for _ in range(M + 1)]
    cameFrom = [v for v in range(M + 1)]
    cameFrom[start] = start
    distance[start] = 0
    hp = [(0, start)]
    resultDist = -1
    meetingScheduleResult = []
    while hp:
        dist, curNode = heapq.heappop(hp)
        if dist > distance[curNode]:
            continue

        if curNode == M - 1:
            resultDist = dist
            meetingScheduleResult = getMeetingSchedule(cameFrom, curNode)
            break
        for v, c in graph[curNode]:
            newCost = dist + c
            if newCost < distance[v]:
                distance[v] = newCost
                heapq.heappush(hp, (newCost, v))
                cameFrom[v] = curNode
    
    head = ''.join(["Case #", str(idx), ": "])
    if resultDist == -1:
        tail = str(-1)
    else:
        tail = ' '.join([str(v) for v in meetingScheduleResult])
    answer.append(head + tail)

for line in answer:
    print(line)