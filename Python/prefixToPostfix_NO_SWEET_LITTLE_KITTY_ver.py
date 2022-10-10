
numbers = set([str(number) for number in range(1, 10)])

#######################################################################################
# 연산자 수정 하고 싶다면 이곳 말고도 calculate 함수도 수정해줄 것
priority_top_operator = set(['/', '*', '^', '%'])
priority_bottom_operator = set(['+', '-'])
all_operator = set(list(priority_top_operator) + list(priority_bottom_operator))
#######################################################################################

def get_operator_priority(operator):
    if operator in priority_top_operator:
        return 1
    elif operator in priority_bottom_operator:
        return 0
        # 

def change_prefix_to_postfix(prefix):
    # 1. 숫자가 나오면 그대로 postfix에 삽입한다.
    # 2. (나오면 스택에 push한다.
    # 3. 우선순위 상 연산자가(*,/,%,^) 나오면 스택에 push한다.
    # 4. 우선순위 하 연산자가(+,-) 나오면 자신 보다 연산 우선 순위가 같거나 높은 연산자가 없을 때 까지 stack에서 pop하여 postfix에 삽입
    # 5. 닫는 괄호(')')가 나오면 여는 괄호('(')가 나올때까지 pop하여 postfix에 삽입한다.
    
    postfix = []
    stack = []
    for letter in prefix:
        if letter in numbers:
            postfix.append(letter)
        elif letter in priority_top_operator:
            stack.append(letter)
        elif letter in priority_bottom_operator:
            # 자신 보다 연산 우선 순위가 같거나 높은 연산자가 없을 때 까지 stack에서 pop하여 postfix에 삽입
            while stack:
                if not (stack[-1] in all_operator) or get_operator_priority(stack[-1]) < get_operator_priority(letter):
                    break
                popped_operator = stack.pop()
                postfix.append(popped_operator)

            # 자신보다 연산 우선 순위가 같거나 높은게 바로 아래 없으면 stack에 append
            stack.append(letter)
        elif letter == '(':
            stack.append(letter)
        elif letter == ')':
            # '(' 나올때 까지 stack에서 pop하여 postfix에 삽입 
            while stack:
                popped_letter = stack.pop()
                if popped_letter == '(':
                    break
                postfix.append(popped_letter)

    # 스택에 남아있는 것 모두 pop
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)

def calculate(num1, num2, operator):
    if operator == '/':
        return num1 / num2
    elif operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '%':
        return num1 % num2
    elif operator == '^':
        return num1 ** num2
    elif operator == '*':
        return num1 * num2
    else:
        print('Im in calculate :', "num1:", num1, "num2:", num2, "operator:", operator)
        raise ValueError()
    # else:

def calculate_postfix(postfix):
    stack = []
    for letter in postfix:
        if letter in all_operator:
            back_num = int(stack.pop())
            front_num = int(stack.pop())
            temp_result = calculate(front_num, back_num, letter)
            stack.append(temp_result)
            print(front_num, letter, back_num, '=', temp_result)
        elif letter in numbers:
            stack.append(letter)
    return stack[0]

import sys

while True:
    print("Input expression:")
    infix_read = ''.join(sys.stdin.readline().strip().split())

    postfix = change_prefix_to_postfix(infix_read)
    print("Postfix is", ' '.join(postfix))

    print("Evaluation starts....")
    result = calculate_postfix(postfix)

    print("Evaluation finishes: The result is", result)