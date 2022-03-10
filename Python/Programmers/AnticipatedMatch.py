def solution(n,a,b):
    answer = 0
    tmp_n = n
    while tmp_n > 1:
        tmp_n /= 2
        answer += 1
        
    if a > b:
        a, b = b, a
    
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        if a <= mid and mid < b:
            break
        elif a < mid and b <= mid:
            right = mid - 1
        else:
            left = mid + 1
        
        answer -= 1
        
    return answer