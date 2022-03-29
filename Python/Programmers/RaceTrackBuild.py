def solution(board):
    s_cost = 100
    t_cost = 500
    # 동서남북
    di = [0, 0, 1, -1]
    dj = [-1, 1, 0, 0]
    dirs = [0, 1, 2, 3]
    n = len(board)
    INF = int(1e6)
    distance = [[INF] * n for _ in range(n)]
    
    distance[0][0] = 0
    
    # i, j, dir, cost
    stack = [(0, 0, 1), (0, 0, 2)]
    while stack:
        ci, cj, cdir = stack.pop()
        if ci == n - 1 and cj == n - 1:
            continue
        for ndir in range(4):
            ni = ci + di[ndir]
            nj = cj + dj[ndir]
            if not(0 <= ni <= n - 1 and 0 <= nj <= n - 1):
                continue
            if board[ni][nj] == 1:
                continue
            # 같은 방향일 경우
            if ndir == cdir:
                new_dist = distance[ci][cj] + s_cost
                if distance[ni][nj] >= new_dist:
                    distance[ni][nj] = new_dist
                    stack.append((ni, nj, ndir))
            else:
                # 방향이 다를 경우
                #if ((cdir == 1 and ndir == 0) or
                #    (cdir == 0 and ndir == 1) or
                #    (cdir == 2 and ndir == 3) or
                #    (cdir == 3 and ndir == 2)):
                #    continue
                new_dist = distance[ci][cj] + s_cost + t_cost
                if distance[ni][nj] >= new_dist:
                    distance[ni][nj] = new_dist
                    stack.append((ni, nj, ndir))
    for line in distance:
        print(line)
    answer = distance[n - 1][n - 1]
    return answer


# 3차원 dist 배열, 각 좌표마다 4방향 최소 거리 저장
# 11, 19 시간 초과

def solution(board):
    n = len(board)
    INF = int(1e6)
    
    s_cost = 100
    t_cost = 500
    # 동서남북
    di = [0, 0, 1, -1]
    dj = [-1, 1, 0, 0]
    dirs = [0, 1, 2, 3]
    distance = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    # distance = [[INF] * n for _ in range(n)]
    
    for i in range(4):
        distance[0][0][i] = 0
    
    # i, j, dir, cost
    stack = [(0, 0, 1), (0, 0, 2)]
    while stack:
        ci, cj, cdir = stack.pop()
        if ci == n - 1 and cj == n - 1:
            continue
        for ndir in range(4):
            ni = ci + di[ndir]
            nj = cj + dj[ndir]
            if not(0 <= ni <= n - 1 and 0 <= nj <= n - 1):
                continue
            if board[ni][nj] == 1:
                continue
            new_dist = distance[ci][cj][cdir] + s_cost if ndir == cdir else distance[ci][cj][cdir] + s_cost + t_cost
            if distance[ni][nj][ndir] > new_dist:
                distance[ni][nj][ndir] = new_dist
                stack.append((ni, nj, ndir))
                
            
    #for line in distance:
    #    print(line)
    answer = min(distance[n - 1][n - 1])
    return answer



# 큐

from collections import deque

def solution(board):
    n = len(board)
    INF = int(1e6)
    
    s_cost = 100
    t_cost = 500
    # 동서남북
    di = [0, 0, 1, -1]
    dj = [-1, 1, 0, 0]
    dirs = [0, 1, 2, 3]
    distance = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    # distance = [[INF] * n for _ in range(n)]
    
    for i in range(4):
        distance[0][0][i] = 0
    
    q = deque([(0, 0, 1, 0), (0, 0, 2, 0)])
    
    # i, j, dir, cost
    # stack = [(0, 0, 1), (0, 0, 2)]
    while q:
        ci, cj, cdir, cur_cost = q.popleft()
        if ci == n - 1 and cj == n - 1:
            continue
        for ndir in range(4):
            ni = ci + di[ndir]
            nj = cj + dj[ndir]
            if not(0 <= ni <= n - 1 and 0 <= nj <= n - 1):
                continue
            if board[ni][nj] == 1:
                continue
            new_dist = cur_cost + s_cost if ndir == cdir else cur_cost + s_cost + t_cost
            if distance[ni][nj][ndir] > new_dist:
                distance[ni][nj][ndir] = new_dist
                q.append((ni, nj, ndir, new_dist))
                
    answer = min(distance[-1][-1])
    return answer