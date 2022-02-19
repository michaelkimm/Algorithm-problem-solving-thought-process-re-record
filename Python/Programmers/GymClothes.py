def solution(n, lost, reserve):
    lost_ary = [False] * (n + 1)
    for num in lost:
        lost_ary[num] = True
        
    reserve_ary = [False] * (n + 1)
    for num in reserve:
        reserve_ary[num] = True

    for num in range(1, n + 1):
        if not lost_ary[num]:
            continue

        if reserve_ary[num]:
            lost_ary[num] = False
            reserve_ary[num] = False
        elif num - 1 >= 0 and reserve_ary[num - 1] and not lost_ary[num - 1]:
            lost_ary[num] = False
            reserve_ary[num - 1] = False
        elif num + 1 <= n and reserve_ary[num + 1] and not lost_ary[num + 1]:
            lost_ary[num] = False
            reserve_ary[num + 1] = False

    answer = 0
    for num in range(1, n + 1):
        if not lost_ary[num]:
            answer += 1
    return answer