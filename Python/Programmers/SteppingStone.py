def solution(distance, rocks, n):
    rocks.sort()
    left, right = 0, distance
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        #
        del_cnt = 0
        std_rock = 0
        for rock in rocks:
            if rock - std_rock < mid:
                del_cnt += 1
            else:
                std_rock = rock
            if del_cnt > n:
                break
        if del_cnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer