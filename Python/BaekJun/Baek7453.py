from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
As = []
Bs = []
Cs = []
Ds = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    As.append(a)
    Bs.append(b)
    Cs.append(c)
    Ds.append(d)

abSumsCnt = defaultdict(int)
answer = 0
for v1 in As:
    for v2 in Bs:
        abSumsCnt[v1 + v2] += 1

for v1 in Cs:
    for v2 in Ds:
        sumVal = v1 + v2
        if -sumVal in abSumsCnt:
            answer += abSumsCnt[-sumVal]

print(answer)