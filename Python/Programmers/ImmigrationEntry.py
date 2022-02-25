from bisect import bisect_left

def solution(n, times):
    left, right = 1, max(times) * n
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        people_passed = 0
        for time in times:
            people_passed += mid // time
        if people_passed >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    return answer