def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for s_v in stones:
            if s_v - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left