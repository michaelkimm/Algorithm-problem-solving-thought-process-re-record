import heapq

def solution(operations):
    hp = []
    for operation in operations:
        cur_oper = operation.split()
        if cur_oper[0] == 'I':
            value = int(cur_oper[1])
            heapq.heappush(hp, value)
        else:
            if not hp:
                continue
            if cur_oper[1] == '1':
                hp = heapq.nlargest(len(hp), hp)[1:]
                heapq.heapify(hp)
            else:
                heapq.heappop(hp)
    
    result = []
    if hp:
        result.append(max(hp))
        result.append(min(hp))
    else:
        result.append(0)
        result.append(0)
    answer = result
    return answer

# ===================================================== #

import heapq

def solution(operations):
    hp = []
    max_hp = []
    for operation in operations:
        cur_oper = operation.split()
        if cur_oper[0] == 'I':
            value = int(cur_oper[1])
            heapq.heappush(hp, value)
            heapq.heappush(max_hp, (-value, value))
        else:
            if not hp:
                continue
            if cur_oper[1] == '1':
                value = heapq.heappop(max_hp)[1]
                hp.remove(value)
                heapq.heapify(hp)
            else:
                value = heapq.heappop(hp)
                max_hp.remove((-value, value))
                heapq.heapify(max_hp)
    result = []
    if not hp:
        result = [0, 0]
    else:
        result = [heapq.heappop(max_hp)[1], heapq.heappop(hp)]
    return result