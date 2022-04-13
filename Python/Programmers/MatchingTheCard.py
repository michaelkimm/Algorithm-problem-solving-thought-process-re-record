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


# ============================================================================= #

from collections import deque
from collections import defaultdict
from itertools import permutations
from itertools import product

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
        
def my_permutation(card_types):
    ary01 = list(product(range(2), repeat=len(card_types)))     # [(0,1), (1,1)]
    ary_types = list(permutations(card_types, len(card_types)))  # [(3,4), (5,2)]
    result = [] # [[(3,0), (4, 1)], [(5,1), (2, 1)]]
    for i in range(len(ary_types)):
        for j in range(len(ary01)):
            tmp = []
            for k in range(len(ary_types[i])):
                tmp.append((ary_types[i][k], ary01[j][k]))
            result.append(tmp)
    #print(len(result))
    return result

def solution(board, r, c):
    # 뒤집을 카드 위치
    card_list = []
    card_dict = defaultdict(list)
    card_types = set()
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_types.add(board[i][j])
                card_dict[board[i][j]].append((i, j))
                card_list.append((board[i][j], i, j))
    permu_result = my_permutation(list(card_types))

    # 모든 경우의 수 계산
    min_key_control_cnt = int(1e10)
    for case in permu_result:
        fliped = [False] * 7
        new_board = [[board[i][j] for j in range(4)] for i in range(4)]
        si, sj = r, c
        key_control_cnt = 0
        for num, card_type in case:
            if fliped[num]:
                continue
            # 현재 위치 -> 카드1 위치
            card1_i, card1_j = card_dict[num][card_type]
            key_control_cnt += bfs(new_board, si, sj, card1_i, card1_j)
            key_control_cnt += 1
            new_board[card1_i][card1_j] = 0
            # 카드1 위치 -> 카드2 위치
            card_type = 1 if card_type == 0 else 0
            card2_i, card2_j = card_dict[num][card_type]
            key_control_cnt += bfs(new_board, card1_i, card1_j, card2_i, card2_j)
            key_control_cnt += 1
            new_board[card2_i][card2_j] = 0
            
            fliped[num] = True
            si, sj = card2_i, card2_j
        min_key_control_cnt = min(min_key_control_cnt, key_control_cnt)
    return min_key_control_cnt