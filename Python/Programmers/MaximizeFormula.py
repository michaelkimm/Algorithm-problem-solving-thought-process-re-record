from itertools import permutations
from collections import deque
import re

def my_operator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    else:
        return a * b

def solution(expression):
    operators = ['+', '-', '*']
    
    expression_q = deque([])
    tmp = ""
    for ch in expression:
        if ch in operators:
            expression_q.append(int(tmp))
            expression_q.append(ch)
            tmp = ""
        else:
            tmp += ch
    expression_q.append(int(tmp))
  
    result = []
    for operator_priority in permutations(operators, len(operators)):
        expression_q1 = deque([v for v in expression_q])
        expression_q2 = deque([])
        for operator in operator_priority:
            
            while expression_q1:
                left_v = expression_q1.popleft()
                if isinstance(left_v, str) and left_v == operator:
                    next_num = expression_q1.popleft()
                    expression_q2[-1] = my_operator(expression_q2[-1], next_num, operator)
                else:
                    expression_q2.append(left_v)
            expression_q1, expression_q2 = expression_q2, expression_q1
            if len(expression_q1) == 1:
                result.append(abs(expression_q1[0]))
                break
            
            
    answer = max(result)
    return answer

    # =================================================== #