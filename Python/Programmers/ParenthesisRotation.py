from collections import deque

def check_right_parenthesis(ary):
    parenthesis = [')', ']', '}']
    stack = []
    for c in ary:
        if c == '(':
            stack.append(')')
        elif c == '[':
            stack.append(']')
        elif c == '{':
            stack.append('}')
        else:
            # )]} 경우
            for p in parenthesis:
                if c == p:
                    if len(stack) > 0 and stack[-1] == p:
                        stack.pop()
                        break
                    else:
                        return False
        
    return len(stack) == 0
            

def solution(s):
    q = deque(s)
    answer = 0
    for x in range(len(s)):
        if check_right_parenthesis(s[x:] + s[:x]):
            answer += 1
    return answer