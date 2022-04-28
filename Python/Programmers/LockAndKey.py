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
    # print(r1, c1, r2, c2)
    result = [ary[i][j] for i in range(r1, r2 + 1) for j in range(c1, c2 + 1)]
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
    for i in range(m):
        for j in range(m):
            if not islock:
                result[i + ci][j + cj] = data[i][j]
            else:
                result[i + ci][j + cj] = data[i][j] if data[i][j] == 1 else -1
    return result

def solution(key, lock):
    n = len(lock)
    m = len(key)
    zero_cnt = 0
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                zero_cnt += 1
    key[2][0] = 1
    keys = get4turnedAry(key)
    expandedLock = getExpandedArray(lock, m, m, n, m, True)
    expandedKey = getExpandedArray(keys[1], m + 1, m + 1, n, m, False)
    print(check(expandedKey, expandedLock, zero_cnt))
    for line in expandedLock:
        print(line)
    print("---")
    for line in expandedKey:
        print(line)
    for i in range(n + m):
        for j in range(n + m):
            for k in keys:
                expandedKey = getExpandedArray(k, i, j, n, m, False)
                if check(expandedKey, expandedLock, zero_cnt):
                    return True
    return False