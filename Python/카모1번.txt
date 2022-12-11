from itertools import combinations
import heapq

INF = int(1e10)

def dijkstra(start, graph):
    # 상대는 안되고 나는 되는 것 먼저 그 다음엔 아무거나 okay
    distance = [INF for _ in range(len(graph))]
    distance[start] = 0
    hp = [(0, start)]
    while hp:
        dist, cur_node = heapq.heappop(hp)
        if distance[cur_node] < dist:
            continue
        for v, c in graph[cur_node]:
            new_cost = dist + c
            if new_cost < distance[v]:
                distance[v] = new_cost
                heapq.heappush(hp, (new_cost, v))
    return distance    

def update_user_info(users, node, user_cnt, parked_cnt, limit):
    parkable_left_cnt = limit - parked_cnt
    if users[node - 1] <= parkable_left_cnt:
        parkable_left_cnt -= users[node - 1]
        user_cnt += users[node - 1]
        users[node - 1] = 0
    else:
        user_cnt += parkable_left_cnt
        users[node - 1] -= parkable_left_cnt
        parkable_left_cnt = 0
    return user_cnt, parkable_left_cnt

def solution(n, edges, users, d, limit):
    graph = [[] for _ in range(n + 1)]
    for u, v, dist in edges:
        graph[u].append((v, dist))
        graph[v].append((u, dist))

    parking_zone_cases = list(combinations([v for v in range(1, n + 1)], 2))
    max_user_cnt = 0
    for case in parking_zone_cases:

        tmp_users = [v for v in users]
        dist_place1 = dijkstra(case[0], graph)
        dist_place2 = dijkstra(case[1], graph)
        place1_parked_cnt = 0
        place2_parked_cnt = 0

        tmp_user_cnt = 0
        # dist_place1, 나만 도달 할 수 있는 유저 수 get
        for node in range(1, n + 1):
            if tmp_users[node - 1] <= 0 or place1_parked_cnt >= limit:
                continue
            if dist_place1[node] > d:
                continue
            if dist_place2[node] <= d:
                continue
            tmp_user_cnt, place1_parked_cnt = update_user_info(tmp_users, node, tmp_user_cnt, place1_parked_cnt, limit)
        # dist_place1, 둘다 도달 할 수 있는 유저 수 get
        for node in range(1, n + 1):
            if tmp_users[node - 1] <= 0 or place1_parked_cnt >= limit:
                continue
            if dist_place1[node] > d:
                continue
            if dist_place2[node] > d:
                continue
            tmp_user_cnt, place1_parked_cnt = update_user_info(tmp_users, node, tmp_user_cnt, place1_parked_cnt, limit)
        # dist_place2, 도달 할 수 있는 유저 수 get
        for node in range(1, n + 1):
            if tmp_users[node - 1] <= 0 or place2_parked_cnt >= limit:
                continue
            if dist_place1[node] > d:
                continue
            if dist_place2[node] > d:
                continue
            tmp_user_cnt, place2_parked_cnt = update_user_info(tmp_users, node, tmp_user_cnt, place2_parked_cnt, limit)
        # dist_place2, 나만 도달 할 수 있는 유저 수 get
        for node in range(1, n + 1):
            if tmp_users[node - 1] <= 0 or place2_parked_cnt >= limit:
                continue
            if dist_place2[node] > d:
                continue
            if dist_place1[node] <= d:
                continue
            tmp_user_cnt, place2_parked_cnt = update_user_info(tmp_users, node, tmp_user_cnt, place2_parked_cnt, limit)
        max_user_cnt = max(max_user_cnt, tmp_user_cnt)

    return max_user_cnt