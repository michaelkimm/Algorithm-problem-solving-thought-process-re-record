def solution(arr):
    # 탈출 조건
    if len(arr) == 1:
        is_one = True if arr[0][0] == 1 else False
        return [0, 1] if is_one else [1, 0]
    
    # 분할 조건
    start_one = True if arr[0][0] == 1 else False
    need_divide = False
    for i in range(len(arr)):
        for j in range(len(arr)):
            if start_one:
                if arr[i][j] == 0:
                    need_divide = True
                    break
            else:
                if arr[i][j] == 1:
                    need_divide = True
                    break
        if need_divide:
            break
            
    zero_total, one_total = 0, 0
    if not need_divide:
        if start_one:
            return [0, 1]
        else:
            return [1, 0]
    else:
        # [0-2][0-2] / [0-2][2-4] / [2-4][0-2] / [2-4][2-4]
        for i in range(0, len(arr) - len(arr) // 2 + 1, len(arr) // 2):
            for j in range(0, len(arr) - len(arr) // 2 + 1, len(arr) // 2):
                tmp_result = solution([row[j:j + len(arr) // 2] for row in arr[i:i + len(arr) // 2]])
                zero_total += tmp_result[0]
                one_total += tmp_result[1]
    
    answer = [zero_total, one_total]
    return answer