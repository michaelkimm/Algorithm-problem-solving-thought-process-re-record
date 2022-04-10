def solution(dirs):
    dir_dict = {'U':0, 'D':1, 'L':2, 'R':3}
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    passed = set()
    answer = 0
    x, y = 0, 0
    for d in dirs:
        dir_idx = dir_dict[d]
        nx = x + dx[dir_idx]
        ny = y + dy[dir_idx]
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue
        if (not (x, y, dx[dir_idx], dy[dir_idx]) in passed) and (not (nx, ny, -dx[dir_idx], -dy[dir_idx]) in passed):
            passed.add((x, y, dx[dir_idx], dy[dir_idx]))
            answer += 1
        x, y = nx, ny
    return answer