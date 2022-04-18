from collections import deque
def check_movable(pos_set, movement, board):
    next_pos_set = set()
    c1, c2 = list(pos_set)
    result = False
    # 우측 이동 경우
    if movement == 0:
        if board[c1[0]][c1[1] + 1] == 0 and board[c2[0]][c2[1] + 1] == 0: 
            next_pos_set = set((c1[0], c1[1] + 1), (c2[0], c2[1] + 1))
            result = True
    # 아래 이동
    elif movement == 1: 
        if board[c1[0] + 1][c1[1]] == 0 and board[c2[0] + 1][c2[1]] == 0: 
            next_pos_set = set((c1[0] + 1, c1[1]), (c2[0] + 1, c2[1]))
            result = True
    # 아래 두개가 0이어야 하는 경우
    elif movement == 2 or movement == 3:
        is_bottom_zero = board[c1[0] + 1][c1[1]] == 0 and board[c2[0] + 1][c2[1]] == 0
        lying = c1[0] == c2[0]
        if is_bottom_zero and lying:
            result = True
            if movement == 2:
                # 시작 가로 / 우측 기준 반시계 회전
                next_pos_set = set((c2[0], c2[1]), (c2[0] + 1, c2[1]))
            elif movement == 3:
                # 시작 가로 / 좌측 기준 시계 회전
                next_pos_set = set((c1[0], c1[1]), (c1[0] + 1, c1[1]))
        
    # 위에 두개가 0이어야 하는 경우
        # 시작 가로 / 우측 기준 시계 회전
        # 시작 가로 / 좌측 기준 반시계 회전
    
    # 우측 두개가 0이어야 하는 경우
        # 시작 세로 / 위 기준 반시계 회전
        # 시작 세로 / 아래 기준 시계 회전
    
    # 좌측 두개가 0이어야 하는 경우
        # 시작 세로 / 위 기준 시계 회전
        # 시작 세로 / 아래 기준 반시계 회전
    
    return True, next_pos_set

def solution(board):
    answer = 0
    N = len(board)
    pos = set([(0,0), (0,1)])
    cost = 0
    q = deque([(pos, cost)])
    visited = set(tuple(pos))
    print(q)
    while True:
        pos_set, cost = q.popleft()
        
        if pos_set == {(N - 1, N - 1), (N - 1, N - 2)} or pos_set == {(N - 1, N - 1), (N - 2, N - 1)}:
            answer = cost
            break
        
        c1, c2 = list(pos_set)
        movable_poses = []
        # 우측 이동
        movable_poses.append(set((c1[0], c1[1] + 1), (c2[0], c2[1] + 1)))
        # 아래 이동
        movable_poses.append(set((c1[0] + 1, c1[1]), (c2[0] + 1, c2[1])))
        # 우측 기준 반시계 회전
        movable_poses.append(set((c2[0] + 1, c2[1]), (c2[0], c2[1])))
        # 좌측 기준 시계 회전
        movable_poses.append(set((c1[0], c1[1]), (c1[0] + 1, c1[1])))
        for next_pos_set in movable_poses:
            next_pos_set = set(list(next_pos_set).sorted(key=lambda x:(x[0], x[1])))
            if not tuple(next_pos_set) in visited and check_movable(pos_set, next_pos_set, board):
                visited.add(tuple(next_pos_set))
                q.append(next_pos_set, cost + 1)
    return answer