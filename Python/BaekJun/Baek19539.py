import sys
input = sys.stdin.readline

N = int(input())
trees = list(map(int, input().split()))

a = 0
b = 0
sum = 0
for i in range(N):
    a += trees[i] // 2
    b += 1 if trees[i] % 2 == 1 else 0
    sum += trees[i]

print("a:", a)
print("b:", b)
print(sum % 3)
print((a + sum // 3) % 3)

print('YES' if (sum % 3 == 0 and a >= b and (a - b) % 3 == 0) else 'NO')