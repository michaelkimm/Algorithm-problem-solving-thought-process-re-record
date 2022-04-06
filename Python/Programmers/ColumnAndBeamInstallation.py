def available(result):
    for x, y, structure in result:
        if structure == 0:
            # 기둥인 경우 / 바닥 / 기둥 아래 기둥 / 기둥 아래 보
            if not (y == 0 or
                (x, y - 1, 0) in result or
                (x, y, 1) in result or
                (x - 1, y, 1) in result):
                return False
        else:
            # 보인 경우 
            if not (((x - 1, y, 1) in result and (x + 1, y, 1) in result) or
                (x, y - 1, 0) in result or (x + 1, y - 1, 0) in result):
                return False
            
    return True
def solution(n, build_frame):
    result = set()
    for x, y, structure, cmd in build_frame:
        if cmd == 1:
            result.add((x, y, structure))
            if not available(result):
                result.remove((x, y, structure))
        else:
            result.remove((x, y, structure))
            if not available(result):
                result.add((x, y, structure))
            
    return sorted(result, key=lambda x:(x[0], x[1], x[2]))