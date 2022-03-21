def solution(N, road, K):
    answer = 0
    INF = int(1e10)
    dp = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][i] = 0
    for a, b, c in road:
        if dp[a][b] <= c:
            continue
        dp[a][b] = c
        dp[b][a] = c
    
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    
    for i in range(1, N + 1):
        if K >= dp[1][i]:
            answer += 1

    return answer

# =============================================================== #

import heapq

def solution(N, road, K):
    answer = 0
    INF = int(1e10)
    distance = [INF] * (N + 1)
    start = 1
    graph = [[] for i in range(N + 1)]
    for a,b,c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리가 가장 짧은 노드 정보 출력
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1

    return answer