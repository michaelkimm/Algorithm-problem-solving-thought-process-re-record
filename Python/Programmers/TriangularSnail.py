def solution(n):
    houses = [[0] * i for i in range(1, n + 1)]
    # 진행 방향 / 하, 우, 상
    direction = [0, 1, 2]
    cur_dir = 0
    d_idx, r_idx, u_idx = 0, 0, -1
    cur_row = 0
    num = 1
    changed = False
    while True:
        # 내려 갈 때 / 아래 현재 row가 0이 아닐 때 까지
        if cur_dir == 0:
            if not(0 <= cur_row < len(houses)) or not (0 <= d_idx < len(houses[cur_row])) or houses[cur_row][d_idx] != 0:
                break
            houses[cur_row][d_idx] = num
            num += 1
            cur_row += 1
            if len(houses) > cur_row and houses[cur_row][d_idx] == 0:
                continue
            else:
                cur_row -= 1
                cur_dir = 1
                d_idx += 1
                r_idx = d_idx
        # 우측 갈 때 / 다음 row가 0이 아닐 때 까지
        if cur_dir == 1:
            if not(0 <= cur_row < len(houses)) or not (0 <= r_idx < len(houses[cur_row])) or houses[cur_row][r_idx] != 0:
                break
            houses[cur_row][r_idx] = num
            num += 1
            r_idx += 1
            if len(houses[cur_row]) > r_idx and houses[cur_row][r_idx] == 0:
                continue
            else:
                cur_row -= 1
                cur_dir = 2
        # 위로 갈 때 / 뒤쪽에서 같은 번째 row가 0이 아닐 때 까지
        if cur_dir == 2:
            if not(0 <= cur_row < len(houses)) or not (-1 * len(houses[cur_row]) <= u_idx < 0) or houses[cur_row][u_idx] != 0:
                break
            houses[cur_row][u_idx] = num
            num += 1
            cur_row -= 1
            if houses[cur_row][u_idx] == 0:
                continue
            else:
                cur_row += 2
                cur_dir = 0
                u_idx -= 1
    answer = []
    for line in houses:
        answer += line
    return answer

# 경계 조건 처리

def solution(n):
    if n == 1:
        return [1]
    
    houses = [[0] * i for i in range(1, n + 1)]
    # 진행 방향 / 하, 우, 상
    direction = [0, 1, 2]
    cur_dir = 0
    d_idx, r_idx, u_idx = 0, 0, -1
    cur_row = 0
    num = 1
    changed = False
    while True:
        # 내려 갈 때 / 아래 현재 row가 0이 아닐 때 까지
        if cur_dir == 0:
            if houses[cur_row][d_idx] != 0:
                break
            houses[cur_row][d_idx] = num
            num += 1
            cur_row += 1
            if len(houses) > cur_row and houses[cur_row][d_idx] == 0:
                continue
            else:
                cur_row -= 1
                cur_dir = 1
                d_idx += 1
                r_idx = d_idx
        # 우측 갈 때 / 다음 row가 0이 아닐 때 까지
        if cur_dir == 1:
            if houses[cur_row][r_idx] != 0:
                break
            houses[cur_row][r_idx] = num
            num += 1
            r_idx += 1
            if len(houses[cur_row]) > r_idx and houses[cur_row][r_idx] == 0:
                continue
            else:
                cur_row -= 1
                cur_dir = 2
        # 위로 갈 때 / 뒤쪽에서 같은 번째 row가 0이 아닐 때 까지
        if cur_dir == 2:
            if houses[cur_row][u_idx] != 0:
                break
            houses[cur_row][u_idx] = num
            num += 1
            cur_row -= 1
            if houses[cur_row][u_idx] == 0:
                continue
            else:
                cur_row += 2
                cur_dir = 0
                u_idx -= 1
    answer = []
    for line in houses:
        answer += line
    return answer


