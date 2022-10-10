import sys
input = sys.stdin.readline

total = 0
read = input().strip().split('-')
for idx, line in enumerate(read):
    if line == '':
        continue
    dt = sum(map(int, line.split('+')))
    total += dt if idx == 0 else -dt
    
print(total)