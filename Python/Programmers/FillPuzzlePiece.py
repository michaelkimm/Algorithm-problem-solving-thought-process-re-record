from collections import deque

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def print_2D_array(ary):
    print("====")
    for line in ary:
        print(line)

def block_elements_to_2D_block(block_elements, value):
    row_values = list(zip(*block_elements))[0]
    col_values = list(zip(*block_elements))[1]
    i_min = min(row_values)
    i_max = max(row_values)
    j_min = min(col_values)
    j_max = max(col_values)
    row_size = i_max - i_min + 1
    col_size = j_max - j_min + 1
    block_2d = [[0 if value == 1 else 1 for _ in range(col_size)] for _ in range(row_size)]
    for ei, ej in block_elements:
        block_2d[ei - i_min][ej - j_min] = value

    return block_2d

def get_2D_blocks(array, value):
    N = len(array)
    visited = [[False for _ in range(N)] for _ in range(N)]
    block_elements_lists = []
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            if array[i][j] != value:
                continue
            visited[i][j] = True
            start = (i, j)
            block_elements = [start]
            q = deque([start])
            while q:
                ci, cj = q.popleft()
                for dirIdx in range(4):
                    ni = ci + di[dirIdx]
                    nj = cj + dj[dirIdx]
                    if not (0 <= ni < N and 0 <= nj < N):
                        continue
                    if visited[ni][nj]:
                        continue
                    if array[ni][nj] != value:
                        continue
                    visited[ni][nj] = True
                    block_elements.append((ni, nj))
                    q.append((ni, nj))
            block_elements_lists.append(block_elements)
    
    blocks = []
    for block_elements in block_elements_lists:
        block_2D = block_elements_to_2D_block(block_elements, value)
        blocks.append(block_2D)
    return blocks

def cross_flip_and_horizontal_flip(ary):
    return [line[::-1] for line in list(zip(*ary))]

def clone_2D_array(ary):
    return [[ary[i][j] for j in range(len(ary[0]))] for i in range(len(ary))]

def get_spinned_blocks(table_block):
    original_block = clone_2D_array(table_block)
    spinned_once = cross_flip_and_horizontal_flip(original_block)
    spinned_twice = cross_flip_and_horizontal_flip(spinned_once)
    spinned_third = cross_flip_and_horizontal_flip(spinned_twice)
    return [original_block, spinned_once, spinned_twice, spinned_third]
    
def match_size(spinned_table_block, game_board_block):
    return len(spinned_table_block) == len(game_board_block) and len(spinned_table_block[0]) == len(game_board_block[0])

def match(ary1, ary2):
    result = 0
    for i in range(len(ary1)):
        for j in range(len(ary1[0])):
            if ary1[i][j] == ary2[i][j]:
                return False
    return True

def get_valid_size(ary, value):
    result = 0
    for i in range(len(ary)):
        for j in range(len(ary[0])):
            if ary[i][j] == value:
                result += 1
    return result

def solution(game_board, table):
    
    answer = 0
    
    table_blocks = get_2D_blocks(table, 1)
    game_board_blocks = get_2D_blocks(game_board, 0)
    game_board_block_used = [False for _ in range(len(game_board_blocks))]
    
    for table_block in table_blocks:
        for i, game_board_block in enumerate(game_board_blocks):
            if game_board_block_used[i]:
                continue
            for spinned_table_block in get_spinned_blocks(table_block):
                if not match_size(spinned_table_block, game_board_block):
                    continue
                if match(spinned_table_block, game_board_block):
                    game_board_block_used[i] = True
                    answer += get_valid_size(game_board_block, 0)
                    break
            if game_board_block_used[i]:
                break
    
    return answer

