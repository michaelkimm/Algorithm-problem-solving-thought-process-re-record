from collections import deque

def check_movable(pos, movement, board):
    next_pos = tuple()
    c1, c2 = pos
    result = False
    is_bottom_zero = (board[c1[0] + 1][c1[1]] == 0 and board[c2[0] + 1][c2[1]] == 0) if c1[0] + 1 < len(board) and c2[0] + 1 < len(board) else False
    is_top_zero = board[c1[0] - 1][c1[1]] == 0 and board[c2[0] - 1][c2[1]] == 0 if c1[0] - 1 >= 0 and c2[0] - 1 >= 0 else False
    is_left_zero = board[c1[0]][c1[1] - 1] == 0 and board[c2[0]][c2[1] - 1] == 0 if c1[1] - 1 >= 0 and c2[1] - 1 >= 0 else False
    is_right_zero = board[c1[0]][c1[1] + 1] == 0 and board[c2[0]][c2[1] + 1] == 0 if c1[1] + 1 < len(board) and c2[1] + 1 < len(board) else False
    lying = c1[0] == c2[0]    
    # 우측 이동 경우
    if movement == 0 or movement == 1:
        if c1[1] + 1 < len(board) and c2[1] + 1 < len(board) and board[c1[0]][c1[1] + 1] == 0 and board[c2[0]][c2[1] + 1] == 0: 
            next_pos = ((c1[0], c1[1] + 1), (c2[0], c2[1] + 1))
            result = True
    # 아래 이동
    elif movement == 2 or movement == 3:
        if c1[0] + 1 < len(board) and c2[0] + 1 < len(board) and board[c1[0] + 1][c1[1]] == 0 and board[c2[0] + 1][c2[1]] == 0:
            next_pos = ((c1[0] + 1, c1[1]), (c2[0] + 1, c2[1]))
            result = True
    # 위로 이동
    # 아래 두개가 0이어야 하는 경우
    elif movement == 4 or movement == 5:
        if is_bottom_zero and lying:
            result = True
            if movement == 4:
                # 시작 가로 / 우측 기준 반시계 회전
                next_pos = ((c2[0], c2[1]), (c2[0] + 1, c2[1]))
            elif movement == 5:
                # 시작 가로 / 좌측 기준 시계 회전
                next_pos = ((c1[0], c1[1]), (c1[0] + 1, c1[1]))
        
    # 위에 두개가 0이어야 하는 경우
    elif movement == 6 or movement == 7:
        if is_top_zero and lying:
            result = True
            if movement == 6:
            # 시작 가로 / 우측 기준 시계 회전
                next_pos = ((c2[0] - 1, c2[1]), (c2[0], c2[1]))      
            elif movement == 7:
            # 시작 가로 / 좌측 기준 반시계 회전
                next_pos = ((c1[0] - 1, c1[1]), (c1[0], c1[1]))      
    
    # 우측 두개가 0이어야 하는 경우
    elif movement == 8 or movement == 9:
        if is_right_zero and not lying:
            result = True
            if movement == 8:
                # 시작 세로 / 위 기준 반시계 회전
                next_pos = ((c1[0], c1[1]), (c1[0], c1[1] + 1))    
            elif movement == 9:
                # 시작 세로 / 아래 기준 시계 회전
                next_pos = ((c2[0], c2[1]), (c2[0], c2[1] + 1))    
    
    # 좌측 두개가 0이어야 하는 경우
    elif movement == 10 or movement == 11:
        if is_left_zero and not lying:
            result = True
            if movement == 10:
                # 시작 세로 / 위 기준 시계 회전
                next_pos = ((c1[0], c1[1] - 1), (c1[0], c1[1]))    
            elif movement == 11:
                # 시작 세로 / 아래 기준 반시계 회전
                next_pos = ((c2[0], c2[1] - 1), (c2[0], c2[1]))    
    # 좌측 이동 경우
    elif movement == 12 or movement == 13:
        if c1[1] - 1 >= 0 and c2[1] - 1 >= 0 and board[c1[0]][c1[1] - 1] == 0 and board[c2[0]][c2[1] - 1] == 0: 
            next_pos = ((c1[0], c1[1] - 1), (c2[0], c2[1] - 1))
            result = True
    # 위 이동
    elif movement == 14 or movement == 15:
        if c1[0] - 1 >= 0 and c2[0] - 1 >= 0 and board[c1[0] - 1][c1[1]] == 0 and board[c2[0] - 1][c2[1]] == 0:
            next_pos = ((c1[0] - 1, c1[1]), (c2[0] - 1, c2[1]))
            result = True
    return result, next_pos

def solution(board):
    answer = 0
    N = len(board)
    pos = ((0,0), (0,1))
    cost = 0
    q = deque([(pos, cost)])
    visited = set([pos])
    while q:
        pos, cost = q.popleft()
        if pos == ((N - 1, N - 2), (N - 1, N - 1)) or pos == ((N - 2, N - 1), (N - 1, N - 1)):
            answer = cost
            break
        
        for movement in range(16):
            movable, next_pos = check_movable(pos, movement, board)
            if movable and not next_pos in visited:
                visited.add(next_pos)
                q.append((next_pos, cost + 1))
    return answer