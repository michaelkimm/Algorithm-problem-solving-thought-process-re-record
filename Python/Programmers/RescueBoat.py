from collections import deque
def solution(people, limit):
    q = deque(sorted(people, reverse=True))
    answer = 0
    
    while len(q) >= 2:
        if q[0] + q[-1] <= limit:
            q.popleft()
            q.pop()
        else:
            q.popleft()
        answer += 1
    if q:
        answer += 1
    return answer

# ================================================ #


from collections import deque
def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    left, right = 0, len(people) - 1
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            left += 1
        answer += 1
        
    return answer