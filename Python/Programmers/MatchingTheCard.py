from collections import deque
def bfs(board, si, sj, target_i, target_j):
    # 동서남북
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    q = deque([(0, si, sj)])
    visited = [[False] * 4 for _ in range(4)]
    visited[si][sj] = True
    cost = int(1e10)
    while q:
        cost, ci, cj = q.popleft()
        if ci == target_i and cj == target_j:
            break
        # 4방향 한칸
        for idx in range(4):
            ni = ci + di[idx]
            nj = cj + dj[idx]
            if 0 <= ni <= 3 and 0 <= nj <= 3 and not visited[ni][nj]:
                q.append((cost + 1, ni, nj))
                visited[ni][nj] = True
        # 4방향 건너뛰기
        for idx in range(4):
            ni, nj = ci, cj
            # 동
            if idx == 0:
                for j in range(cj + 1, 4):
                    if board[ni][j] != 0:
                        nj = j
                        break
                    nj = 3
            # 서
            elif idx == 1:
                for j in range(cj - 1, -1, -1):
                    if board[ni][j] != 0:
                        nj = j
                        break
                    nj = 0
            # 남
            elif idx == 2:
                for i in range(ci + 1, 4):
                    if board[i][nj] != 0:
                        ni = i
                        break
                    ni = 3
            # 북
            elif idx == 3:
                for i in range(ci - 1, -1, -1):
                    if board[i][nj] != 0:
                        ni = i
                        break
                    ni = 0
            if not visited[ni][nj]:
                q.append((cost + 1, ni, nj))
                visited[ni][nj] = True
    return cost
        
def brute_force(board, card_list, si, sj):
    if len(card_list) == 0:
        return 0
    
    results = [0] * len(card_list)
    for idx, card in enumerate(card_list):
        c_num, ci, cj = card
        new_board = [[board[i][j] for j in range(4)] for i in range(4)]
        # si, sj에서 card까지 가기, 뒤집기
        key_control_cnt = bfs(new_board, si, sj, ci, cj)
        key_control_cnt += 1
        new_board[ci][cj] = 0
        
        # card 짝 까지 가기, 뒤집기
        m_c_i, m_c_j = 0, 0
        for c in card_list:
            if c[0] == c_num and not (c[1] == ci and c[2] == cj):
                m_c_i, m_c_j = c[1], c[2]
        key_control_cnt += bfs(new_board, ci, cj, m_c_i, m_c_j)
        key_control_cnt += 1
        new_board[m_c_i][m_c_j] = 0
        results[idx] += key_control_cnt
        
        # 다음 경우의 수 구하기
        new_card_list = [c for c in card_list if c[0] != c_num]
        results[idx] += brute_force(new_board, new_card_list, m_c_i, m_c_j)
    return min(results)
    
def solution(board, r, c):
    # 뒤집을 카드 위치
    card_list = []
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_list.append((board[i][j], i, j))
    
    new_board = [[board[i][j] for j in range(4)] for i in range(4)]
    answer = brute_force(new_board, card_list, r, c)
    return answer

# ======================================================= #

from collections import deque
def move_in(val):
    if val < 0:
        val = 0
    elif val > 3:
        val = 3
    return val

def ctrl_move(board, ci, cj, di, dj):
    ni, nj = ci, cj
    for n in range(1, 4):
        ni = ci + di * n
        nj = cj + dj * n
        if 0 <= ni <= 3 and 0 <= nj <= 3:
            if board[ni][nj] != 0:
                break
    ni = move_in(ni)
    nj = move_in(nj)
    return ni, nj

def bfs(board, si, sj, target_i, target_j):
    # 동서남북
    q = deque([(0, si, sj)])
    visited = [[False] * 4 for _ in range(4)]
    visited[si][sj] = True
    cost = int(1e10)
    while q:
        cost, ci, cj = q.popleft()
        if ci == target_i and cj == target_j:
            break
        # 4방향 한칸
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # 한칸
            ni = ci + di
            nj = cj + dj
            if 0 <= ni <= 3 and 0 <= nj <= 3 and not visited[ni][nj]:
                q.append((cost + 1, ni, nj))
                visited[ni][nj] = True
            # 건너 뛰기
            ni, nj = ctrl_move(board, ci, cj, di, dj)
            if not visited[ni][nj]:
                q.append((cost + 1, ni, nj))
                visited[ni][nj] = True
    return cost
        
def brute_force(board, card_list, si, sj):
    if len(card_list) == 0:
        return 0
    
    results = [0] * len(card_list)
    for idx, card in enumerate(card_list):
        c_num, ci, cj = card
        new_board = [[board[i][j] for j in range(4)] for i in range(4)]
        # si, sj에서 card까지 가기, 뒤집기
        key_control_cnt = bfs(new_board, si, sj, ci, cj)
        key_control_cnt += 1
        new_board[ci][cj] = 0
        
        # card 짝 까지 가기, 뒤집기
        m_c_i, m_c_j = 0, 0
        for c in card_list:
            if c[0] == c_num and not (c[1] == ci and c[2] == cj):
                m_c_i, m_c_j = c[1], c[2]
        key_control_cnt += bfs(new_board, ci, cj, m_c_i, m_c_j)
        key_control_cnt += 1
        new_board[m_c_i][m_c_j] = 0
        results[idx] += key_control_cnt
        
        # 다음 경우의 수 구하기
        new_card_list = [c for c in card_list if c[0] != c_num]
        results[idx] += brute_force(new_board, new_card_list, m_c_i, m_c_j)
    return min(results)
    
def solution(board, r, c):
    # 뒤집을 카드 위치
    card_list = []
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_list.append((board[i][j], i, j))
    
    new_board = [[board[i][j] for j in range(4)] for i in range(4)]
    answer = brute_force(new_board, card_list, r, c)
    return answer