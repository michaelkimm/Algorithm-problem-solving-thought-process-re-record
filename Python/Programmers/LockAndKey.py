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

def check(key, lock, zero_cnt):
    result = True
    cnt = 0
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1 and lock[i][j] == -1:
                cnt += 1
            elif key[i][j] == 1 and lock[i][j] == 1:
                return False
    if zero_cnt != cnt:
        result = False
    return result

def getExpandedArray(data, ci, cj, n, m, islock):
    result = [[0] * (2 * m + n) for _ in range(2 * m + n)]
    if islock:
        for i in range(n):
            for j in range(n):
                result[i + ci][j + cj] = data[i][j] if data[i][j] == 1 else -1
    else:
        for i in range(m):
            for j in range(m):
                result[i + ci][j + cj] = data[i][j]
                
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
    expandedLock = getExpandedArray(lock, m, m, n, m, True)
    for i in range(n + m):
        for j in range(n + m):
            for k in keys:
                expandedKey = getExpandedArray(k, i, j, n, m, False)
                if check(expandedKey, expandedLock, zero_cnt):
                    return True
    return False


# ================================================================= #
def getTargetIndexes(ary, target):
    return [(i, j) for i in range(len(ary)) for j in range(len(ary)) if ary[i][j] == target]

def getRotatedIndexes(ary, m):
    return [(j, m - i - 1) for i, j in ary]

def solution(key, lock):
    n = len(lock)
    m = len(key)
    lock_hole = getTargetIndexes(lock, 0)
    key0_hole = getTargetIndexes(key, 1)
    key90_hole = getRotatedIndexes(key0_hole, m)
    key180_hole = getRotatedIndexes(key90_hole, m)
    key270_hole = getRotatedIndexes(key180_hole, m)
    
    for key in [key0_hole, key90_hole, key180_hole, key270_hole]:
        # key = [(1, 2), (2, 3), (3, 2)]
        for i in range(-1 * m + 1, n + m):
            for j in range(-1 * m + 1, n + m):
                cnt = 0
                for block in key:
                    # block = (1, 2)
                    moved_block_i = block[0] + i
                    moved_block_j = block[1] + j
                    if not (0 <= moved_block_i < n and 0 <= moved_block_j < n):
                        continue
                    if lock[moved_block_i][moved_block_j] == 1:
                        cnt = -1
                        break
                    if lock[moved_block_i][moved_block_j] == 0:
                        cnt += 1
                if cnt == len(lock_hole):
                    return True
    return False