def solution(s):
    answer = True
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                answer = False
                break
    if stack:
        answer = False
    return answer