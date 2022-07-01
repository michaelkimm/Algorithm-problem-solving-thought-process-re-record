def solution(n, times):
    times.sort()
    left = 0
    right = max(times) * n
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        passed_cnt = 0
        for time_cost in times:
            passed_cnt += (mid // time_cost)
        if passed_cnt >= n:
            right = mid - 1
            answer = mid
        elif passed_cnt < n:
            left = mid + 1
            
    return answer