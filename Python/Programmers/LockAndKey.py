def get4turnedAry(ary):
    t90 = Turn2DArrayCW(ary)
    t180 = Turn2DArrayCW(t90)
    t270 = Turn2DArrayCW(t180)
    return [ary, t90, t180, t270]
  
def Turn2DArrayCW(ary):
    rowCnt = len(ary)
    colCnt = len(ary[0])
    result = []
    for colIdx in range(colCnt):
        newRow = []
        for rowIdx in range(rowCnt-1, -1, -1):
            newRow.append(ary[rowIdx][colIdx])
        result.append(newRow)
    return result
  
def Turn2DArrayCWs(ary, rotateCnt):
    result = ary
    for _ in range(rotateCnt):
        result = Turn2DArrayCW(result)
    return result

def truncate_array(ary, r1, c1, r2, c2):
    result = [ary[i][j] for i in range(r1, r2 + 1) for j in range(c1, c2 + 1)]
    return result

def check(key, r1, c1, r2, c2, lock, r3, c3, zero_cnt):
    print(r1,c1,r2,c2)
    truncated_key = truncate_array(key, r1, c1, r2, c2)
    truncated_lock = truncate_array(lock, r3, c3, r3 + (r2 - r1), c3 + (c2 - c1))
    result = True
    cnt = 0
    for i in range(len(truncated_key)):
        if truncated_key[i] == 1 and truncated_lock[i] == 0:
            cnt += 1
        elif truncated_key[i] == truncated_lock[i]:
            result = False
            break
    if zero_cnt != cnt:
        result = False
    return result

def solution(key, lock):
    n = len(lock)
    m = len(key)
    zero_cnt = 0
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                zero_cnt += 1
    keys = get4turnedAry(key)
    target_key = [[0, 1, 0], [1, 0, 0], [1, 0, 0]]
    # 위 -> 중간
    for i in range(1, n + 1):
        # 좌 끝-> 중간 전
        for j in range(1, n + 1):
            for k in keys:
                print(1)
                r1 = m - i if m - i >= 0 else 0
                r2 = m - j if m - j >= 0 else 0
                if check(k, r1, r2, m - 1, m - 1, lock, 0, 0, zero_cnt):
                    return True
        # 중간 -> 우 끝
        for j in range(1, n + 1):
            for k in keys:
                print(2)
                r1 = m - i if m - i >= 0 else 0
                c2 = m - j if m - j >= 0 else 0
                if check(k, r1, m - m, m - 1, c2, lock, 0, j - 1, zero_cnt):
                    return True
    
    # 중간 -> 아래
    for i in range(1, n + 1):
        # 좌 끝-> 중간 전
        for j in range(1, n + 1):
            for k in keys:
                print(3)
                c1 = m - j if m - j >= 0 else 0
                r2 = i - 1 if i - 1 < m else m - 1
                if check(k, 0, c1, r2, m - 1, lock, n - i, 0, zero_cnt):
                    return True
        # 중간 -> 우 끝
        for j in range(1, n + 1):
            for k in keys:
                r2 = i - 1 if i - 1 < m else m - 1
                c2 = m - j if m - j >= 0 else 0
                print(4)
                if check(k, 0, 0, r2, c2, lock, n - i, j - 1, zero_cnt):
                    return True
    
    return False