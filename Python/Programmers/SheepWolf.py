from collections import deque

def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    
    q = deque([(1, 0, 0, set([0]))])    # 양 개수, 늑대 개수, 현재 노드, 모은 노드
    visited = set()
    max_sheep = 0
    while q:
        sheep_cnt, wolf_cnt, node, gathered = q.popleft()
        max_sheep = max(sheep_cnt, max_sheep)
        for next_node in graph[node]:
            next_sheep_cnt = sheep_cnt
            next_wolf_cnt = wolf_cnt
            if not next_node in gathered:
                if info[next_node] == 0:
                    next_sheep_cnt += 1
                else:
                    next_wolf_cnt += 1
            if next_sheep_cnt <= next_wolf_cnt:
                continue
            new_gathered = set([val for val in gathered])
            new_gathered.add(next_node)
            if (next_sheep_cnt, next_wolf_cnt, next_node, tuple(new_gathered)) in visited:
                continue
            q.append((next_sheep_cnt, next_wolf_cnt, next_node, new_gathered))
            visited.add((sheep_cnt, wolf_cnt, node, tuple(new_gathered)))
    return max_sheep