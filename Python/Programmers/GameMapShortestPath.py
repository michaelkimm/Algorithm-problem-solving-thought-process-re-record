from collections import deque
def solution(maps):
    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    answer = -1
    
    # map = n x m
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    # bfs
    start = (0, 0, 1)
    q = deque([start])
    while q:
        ci, cj, cost = q.popleft()
        if ci == len(maps) - 1 and cj == len(maps[0]) - 1:
            answer = cost
            break
        
        for idx in range(4):
            ni = ci + di[idx]
            nj = cj + dj[idx]
            if 0 <= ni < len(maps) and 0 <= nj < len(maps[0]) and maps[ni][nj] == 1 and not visited[ni][nj]:
                q.append((ni, nj, cost + 1))
                visited[ni][nj] = True
    
    # return -1 고려
    return answer