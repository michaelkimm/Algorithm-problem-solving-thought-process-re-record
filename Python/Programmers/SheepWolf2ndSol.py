from collections import deque

def getNewSet(cur_set):
    new_set = set([v for v in cur_set])
    return new_set

def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    pos = 0
    sheep_cnt = 1
    wolf_cnt = 0
    gathered = set([pos])
    q = deque([(sheep_cnt, wolf_cnt, gathered, pos)])
    visited = set([(sheep_cnt, wolf_cnt, tuple(gathered), pos)])
    max_sheep = sheep_cnt
    
    cnt = 0
    
    while q:
        cur_sheep_cnt, cur_wolf_cnt, gathered, cur_pos = q.popleft()
        
        
        if cur_sheep_cnt > max_sheep:
            max_sheep = cur_sheep_cnt
            
        for v in graph[cur_pos]:
            new_gathered = getNewSet(gathered)
            if v in new_gathered:
                if (cur_sheep_cnt, cur_wolf_cnt, tuple(new_gathered), v) in visited:
                    continue
                q.append((cur_sheep_cnt, cur_wolf_cnt, new_gathered, v))
                visited.add((cur_sheep_cnt, cur_wolf_cnt, tuple(new_gathered), v))
                continue
                
            if info[v] == 1:
                if cur_sheep_cnt <= (cur_wolf_cnt + 1):
                    continue
                new_gathered.add(v)
                if (cur_sheep_cnt, cur_wolf_cnt + 1, tuple(new_gathered), v) in visited:
                    continue
                q.append((cur_sheep_cnt, cur_wolf_cnt + 1, new_gathered, v))
                visited.add((cur_sheep_cnt, cur_wolf_cnt + 1, tuple(new_gathered), v))
            else:
                new_gathered.add(v)
                if (cur_sheep_cnt + 1, cur_wolf_cnt, tuple(new_gathered), v) in visited:
                    continue
                q.append((cur_sheep_cnt + 1, cur_wolf_cnt, new_gathered, v))
                visited.add((cur_sheep_cnt + 1, cur_wolf_cnt, tuple(new_gathered), v))
            
    return max_sheep
