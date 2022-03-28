def solution(n, s, a, b, fares):
    INF = int(1e10)
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 0
    for u, v, c in fares:
        dp[u][v] = c
        dp[v][u] = c
    
    for m in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][m] + dp[m][j])
                
    distances = [0] * (n + 1)
    for i in range(1, n + 1):
        distances[i] = dp[s][i] + dp[i][a] + dp[i][b]
        
    answer = min(distances[1:])
    return answer

# =============================================================== #

import heapq

def dijkstra(start, end, graph):
    distance = 0
    return distance

def solution(n, s, a, b, fares):
    INF = int(1e10)
    distance = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for u, v, c in fares:
        graph[u].append((v, c))
        graph[v].append((u, c))
    # s -> 모든 노드
    for node in range(1, n + 1):
        visited = [False] * (n + 1)
        dist = [INF] * (n + 1)
        dist[node] = 0
        hp = [(0, node)]
        while hp:
            cost, cur_node = heapq.heappop(hp)
            if cost > dist[cur_node]:
                continue
            for next_node, nc in graph[cur_node]:
                new_cost = cost + nc
                if new_cost < dist[next_node]:
                    dist[next_node] = new_cost
                    heapq.heappush(hp, (new_cost, next_node))
        distance[node] = dist[s] + dist[a] + dist[b]
    answer = min(distance[1:])
    return answer