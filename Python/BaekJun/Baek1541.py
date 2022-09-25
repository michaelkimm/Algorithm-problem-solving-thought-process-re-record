from collections import deque
import re
import sys
input = sys.stdin.readline 
line = input().strip()

numbers = deque(map(int, re.findall('[0-9]+', line)))
operators = re.findall('[+-]', line)

if len(numbers) == len(operators):
    numbers.appendleft(0)

total = numbers[0]
numbers.popleft()
minusSum = 0

for operator in operators:
    curNum = numbers.popleft()
    if operator == '-':
        if minusSum == 0:
            minusSum += curNum
        else:
            total -= minusSum
            minusSum = curNum
    else:
        if minusSum == 0:
            total += curNum
        else:
            minusSum += curNum

total -= minusSum

print(total)