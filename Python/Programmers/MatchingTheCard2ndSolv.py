from collections import deque

def getCardSetCnt(board):
    need_erased_cnt = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                need_erased_cnt += 1
    need_erased_cnt //= 2
    return need_erased_cnt

def clone2DBoardTo1D(board):
    return ''.join([str(board[row][col]) for row in range(4) for col in range(4)])

def clone1DBoardTo1D(board):
    return ''.join([str(board[idx]) for idx in range(16)])

def moveOneDist(cur_r, cur_c, dr, dc):
    next_r = cur_r + dr
    next_c = cur_c + dc
    return next_r, next_c

def moveWithCtrl(board, cur_r, cur_c, dr, dc):
    next_r, next_c = cur_r, cur_c
    while True:
        next_r += dr
        next_c += dc
        if not(0 <= next_r < 4 and 0 <= next_c < 4):
            next_r -= dr
            next_c -= dc
            break
        if board[get1DIndex(next_r, next_c)] != '0':
            break
    if next_r == cur_r and next_c == cur_c:
      return -1, -1
    return next_r, next_c

def get1DIndex(row, col):
  return row * 4 + col

def solution(board, r, c):
    need_erased_cnt = getCardSetCnt(board)
    
    # 동서남북
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    
    cost = 0
    cur_board = clone2DBoardTo1D(board)
    erased = 0
    entered = '0'
    enteredIdx = -1
    start_node = (cur_board, r, c, cost, erased, entered, enteredIdx)
    q = deque([start_node])
    visited = set()

    cnt = 0
    
    while q:
        cur_node = q.popleft()
        cur_board, cur_r, cur_c, cur_cost, erased, entered, enteredIdx= cur_node
        indexOf1D = get1DIndex(cur_r, cur_c)
        # 탈출 조건
        if (erased == need_erased_cnt):
            cost = cur_cost
            break
            
        if (cur_board, cur_r, cur_c, entered, enteredIdx) in visited:
            continue
        else:
            visited.add((cur_board, cur_r, cur_c, entered, enteredIdx))

        # 한칸 방향키
        for index in range(4):
            next_r, next_c = moveOneDist(cur_r, cur_c, dr[index], dc[index])
            # 나간 경우
            if not(0 <= next_r < 4 and 0 <= next_c < 4):
                continue
            
            # 큐 삽입
            next_board = clone1DBoardTo1D(cur_board)
            q.append((next_board, next_r, next_c, cur_cost + 1, erased, entered, enteredIdx))
        
        # Ctrl + 방향키
        for index in range(4):
            next_r, next_c = moveWithCtrl(cur_board, cur_r, cur_c, dr[index], dc[index])
            if next_r == -1 and next_c == -1:
                continue
            
            # 큐 삽입
            next_board = clone1DBoardTo1D(cur_board)
            q.append((next_board, next_r, next_c, cur_cost + 1, erased, entered, enteredIdx))
        
        # Enter
        # 빈칸 위면 패스
        if cur_board[indexOf1D] == '0':
            continue
        # 엔터가 되있으면 같은 숫자만 엔터,
        elif cur_board[indexOf1D] != '0' and cur_board[indexOf1D] == entered and enteredIdx != indexOf1D:
            next_board = clone1DBoardTo1D(cur_board)
            next_board = next_board.replace(cur_board[indexOf1D], '0')
            
            entered = '0'
            erased += 1
            q.append((next_board, cur_r, cur_c, cur_cost + 1, erased, entered, enteredIdx))
        # 엔터가 안되있으면 그냥 해도 됨.
        elif cur_board[indexOf1D] != '0' and entered == '0':
            entered = cur_board[indexOf1D]
            enteredIdx = indexOf1D
            next_board = clone1DBoardTo1D(cur_board)
            q.append((next_board, cur_r, cur_c, cur_cost + 1, erased, entered, enteredIdx))

    answer = cost
    return answer
