def solution(string):
    stack = []
    for ch in string:
        if not stack or stack[-1] != ch:
            stack.append(ch)
            continue
        elif stack[-1] == ch:
            stack.pop()
    return 0 if stack else 1