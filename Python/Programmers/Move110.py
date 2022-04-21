def move_110(target):
    idx_110 = target.find("110")
    if idx_110 == -1:
        return target
    # 110 추출
    target = target[:idx_110] + target[idx_110 + 3:]
    idx_111 = target.find("111")
    if idx_111 == -1:
        # 맨 끝이 2인 경우
        if len(target) >= 2 and target[len(target) - 2:] == "11": 
            target = target[:len(target) - 2] + "110" + target[len(target) - 2:]
        # 맨 끝이 1인 경우
        elif len(target) >= 1 and target[-1] == '1':
            target = target[:len(target) - 1] + "110" + target[-1]
        # 둘다 아닌 경우
        else:
            target += "110"
    else:
        target = target[:idx_111] + "110" + target[idx_111:]
        target = target[:idx_111 + 3] + move_110(target[idx_111 + 3:])
    
    return target
    
    
    
def solution(s):
    import sys
    limit_number = 200000
    sys.setrecursionlimit(limit_number)
    answer = []
    for source in s:
        answer.append(move_110(source))
    return answer


# ============================================================= #

def move_110(target):
    pop_cnt = 0
    stack = []
    for num in target:
        # 삽입
        stack.append(num)
        # 스택 안이 110이면 세게 다 꺼내고 pop_cnt += 1
        if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
            del stack[-3:]
            pop_cnt += 1
    target = ''.join(stack)
    
    idx_111 = target.find("111")
    string_110 = ''.join(["110" for _ in range(pop_cnt)])
    if idx_111 == -1:
        # 맨 끝이 11인 경우
        if len(target) >= 2 and target[len(target) - 2:] == "11": 
            target = target[:len(target) - 2] + string_110 + target[len(target) - 2:]
        # 맨 끝이 1인 경우
        elif len(target) >= 1 and target[-1] == '1':
            target = target[:len(target) - 1] + string_110 + target[-1]
        # 둘다 아닌 경우
        else:
            target += string_110
    else:
        target = target[:idx_111] + string_110 + target[idx_111:]

    return target
    
def solution(s):
    answer = []
    for source in s:
        answer.append(move_110(source))
    return answer