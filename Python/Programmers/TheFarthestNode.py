import heapq

def solution(n, edge):
    INF = int(1e10)
    
    graph = [[] for _ in range(n + 1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
        
    distance = [INF] * (n + 1)
    start = 1
    hp = [(0, start)]
    distance[start] = 0
    while hp:
        dist, node = heapq.heappop(hp)
        
        # 이미 처리된 적 있는 노드면 패스
        if dist > distance[node]:
            continue
        
        for next_node in graph[node]:
            if distance[next_node] > dist + 1:
                distance[next_node] = dist + 1
                heapq.heappush(hp, (distance[next_node], next_node))
                
    max_val = -1
    max_cnt = 0
    for node in range(1, n + 1):
        if max_val <= distance[node]:
            if max_val == distance[node]:
                max_cnt += 1
            else:
                max_val = distance[node]
                max_cnt = 1
    
    
    answer = max_cnt
    return answer