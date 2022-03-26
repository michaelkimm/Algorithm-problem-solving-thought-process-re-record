from collections import deque

def block_fall(m, n, board_list):
    for j in range(n):
        l = deque()
        for i in range(m - 1, -1, -1):
            # 빈칸이 아니면 큐에 모두 담는다
            if board_list[i][j] != "-":
                l.append(board_list[i][j])
        # 큐가 존재하면 빼서 담고 아니면 빈칸으로 만듬
        for i in range(m - 1, -1, -1):
            board_list[i][j] = l.popleft() if l else "-"
    return

def get_poppable_cnt(i, j, board_list, visited, popped_area):
    m = len(board_list)
    n = len(board_list[0])
    visited[i][j] = True
    popped_cnt = 0
    popped_idxes = []
    # 정사각형 만들 수 없으면 return 0
    for di in range(2):
        for dj in range(2):
            ni = i + di
            nj = j + dj
            if ni >= m or nj >= n:
                return 0
    # 정사각형 만들 수 있는 경우
    # 내부 요소가 다르면 return 0
    if not (board_list[i][j] == board_list[i + 1][j] and
            board_list[i][j] == board_list[i][j + 1] and
            board_list[i][j] == board_list[i + 1][j + 1]):
        return 0
    
    if not ('A' <= board_list[i][j] <= 'Z'):
        return 0
    
    # pop 처리
    for di in range(2):
        for dj in range(2):
            # pop 처리
            ni = i + di
            nj = j + dj
            if not popped_area[ni][nj]:
                #print(ni, nj)
                popped_cnt += 1
                popped_area[ni][nj] = True
                popped_idxes.append((ni, nj))
            
    # 팝한 곳 돌며 동시에 pop할 수 있는지 확인.
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            ni = i + di
            nj = j + dj
            if ni >= m or nj >= n or ni < 0 or nj < 0:
                continue
            # 내부 요소들을 돌며 get_poppable_cnt
            if not visited[ni][nj]:
                popped_cnt += get_poppable_cnt(ni, nj, board_list, visited, popped_area)

    for ni, nj in popped_idxes:
        board_list[ni][nj] = '-'
    return popped_cnt

def rotate_for_deletion(m, n, board_list):
    # 팝된 후 재귀로 해당 구간을 확인한 경우
    visited = [[False] * n for _ in range(m)]
    # 팝이 됬는지
    popped_area = [[False] * n for _ in range(m)]
    deletion_cnt = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                if board_list[i][j] != '-':
                    deletion_cnt = get_poppable_cnt(i, j, board_list, visited, popped_area)
                    if deletion_cnt != 0:
                        return deletion_cnt

    return 0

def solution(m, n, board):
    deleted_cnt = 0
    board_list = [list(line) for line in board]
    new_deletion_cnt = -1
    
    while new_deletion_cnt != 0:
        new_deletion_cnt = rotate_for_deletion(m, n, board_list)
        if new_deletion_cnt != 0:
            # 삭제 갯수 업데이트
            deleted_cnt += new_deletion_cnt
            # 블록 아래로 떨어져 빈 공간 채우기
            block_fall(m, n, board_list)
    return deleted_cnt