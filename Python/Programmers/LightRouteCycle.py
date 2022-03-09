from collections import deque

def get_dir(cur_dir_x, cur_dir_y, ch):
    if ch == 'R':
        return 0 * cur_dir_x + -1 * cur_dir_y, 1 * cur_dir_x + 0 * cur_dir_y 
    elif ch == 'S':
        return cur_dir_x, cur_dir_y
    else:
        return 0 * cur_dir_x + 1 * cur_dir_y, -1 * cur_dir_x + 0 * cur_dir_y 

def dir_to_idx(dir_x, dir_y):
    if dir_x == 0 and dir_y == -1:
        return 0
    elif dir_x == 0 and dir_y == 1:
        return 1
    elif dir_x == -1 and dir_y == 0:
        return 2 
    else:
        return 3 
    
def solution(grid):
    # 상하좌우
    dy = [-1, 1, 0, 0]  
    dx = [0, 0, -1, 1]
    
    # bfs
    start = (0, 0) # i, j, dir_i, dir_j, cost
    cost = 0
    answer = []
    grid3d = [[[False, False, False, False] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            start = (x, y)
            cost = 0
    
            for idx in range(4):
                start_info = (start[0], start[1], dx[idx], dy[idx], cost)
                cur_info = start_info

                while not grid3d[cur_info[1]][cur_info[0]][dir_to_idx(cur_info[2], cur_info[3])]:
                    # 도착 표시
                    grid3d[cur_info[1]][cur_info[0]][dir_to_idx(cur_info[2], cur_info[3])] = True
                    
                    # 다음 좌표, 방향 계산
                    ndir_x, ndir_y = get_dir(cur_info[2], cur_info[3], grid[cur_info[1]][cur_info[0]])
                    nx = cur_info[0] + ndir_x
                    if nx  >= len(grid[0]):
                        nx = 0
                    elif nx < 0:
                        nx = len(grid[0]) - 1

                    ny = cur_info[1] + ndir_y
                    if ny  >= len(grid):
                        ny = 0
                    elif ny < 0:
                        ny = len(grid) - 1
                        
                    cur_info = (nx, ny, ndir_x, ndir_y, cur_info[4] + 1)
                
                if cur_info[4] != start_info[4]:
                    answer.append(cur_info[4])
            
    return sorted(answer)