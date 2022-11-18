import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

cnts = [0 for _ in range(len(T))]

for alphabet in S:
    idx = T.find(alphabet)
    if idx == 0:
        cnts[idx] += 1
    elif idx > 0 and cnts[idx - 1] > 0:
        cnts[idx - 1] -= 1
        cnts[idx] += 1
print(cnts[-1])