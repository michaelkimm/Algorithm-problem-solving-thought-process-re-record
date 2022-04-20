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