def my_rotate(ary, i0, j0, i1, j1):
    min_val = int(10002)
    start_val = ary[i0][j0]
    # 왼쪽
    for i in range(i0, i1):
        ary[i][j0] = ary[i + 1][j0]
        min_val = min(ary[i + 1][j0], min_val)
    # 아래
    for j in range(j0, j1):
        ary[i1][j] = ary[i1][j + 1]
        min_val = min(ary[i1][j + 1], min_val)
    # 오른
    for i in range(i1, i0, -1):
        ary[i][j1] = ary[i - 1][j1]
        min_val = min(ary[i - 1][j1], min_val)
    # 위
    for j in range(j1, j0, -1):
        ary[i0][j] = ary[i0][j - 1]
        min_val = min(ary[i0][j - 1], min_val)
    ary[i0][j0 + 1] = start_val
    min_val = min(start_val, min_val)
    
    return ary, min_val

def solution(rows, columns, queries):
    ary = [[j + columns * i for j in range(1, columns + 1)] for i in range(rows)]
    answer = []
    for i0, j0, i1, j1 in queries:
        ary, min_val = my_rotate(ary, i0 - 1, j0 - 1, i1 - 1, j1 - 1)
        answer.append(min_val)        
    return answer