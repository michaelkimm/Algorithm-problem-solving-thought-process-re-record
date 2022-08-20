from collections import defaultdict
import sys
input = sys.stdin.readline

def getCartasianProductSum(ary1, ary2):
    ret = []
    for v1 in ary1:
        for v2 in ary2:
            ret.append(v1 + v2)
    return ret

def getCountCompaction(ary):
    cnts = defaultdict(int)
    for v in ary:
        cnts[v] += 1
    
    return cnts

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

abSums = getCartasianProductSum(As, Bs)
abSumCompacted = getCountCompaction(abSums)

cdSums = getCartasianProductSum(Cs, Ds)
cdSumCompacted = getCountCompaction(cdSums)

answer = 0

for abSumval, abSumCnt in abSumCompacted.items():
    if cdSumCompacted[-abSumval] != 0:
        answer += (abSumCnt * cdSumCompacted[-abSumval])

print(answer)