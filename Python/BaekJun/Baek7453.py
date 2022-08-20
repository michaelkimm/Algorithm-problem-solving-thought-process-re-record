from collections import defaultdict
import sys
input = sys.stdin.readline

def getCartasianProductSum(ary1, ary2):
    ret = []
    for v1 in ary1:
        for v2 in ary2:
            ret.append(v1 + v2)
    ret.sort()
    return ret

def bisect_left(ary, target):
    left = 0
    right = len(ary) - 1
    ret = -1
    while left <= right:
        mid = (left + right) // 2
        if ary[mid] == target:
            ret = mid
            break
        elif ary[mid] > target:
            right = mid - 1
        elif ary[mid] < target:
            left = mid + 1
    if ret != -1:
        while ret >= 0 and ary[ret] == target:
            ret -= 1
        ret += 1
    return ret

def bisect_right(ary, target):
    left = 0
    right = len(ary) - 1
    ret = -1
    while left <= right:
        mid = (left + right) // 2
        if ary[mid] == target:
            ret = mid
            break
        elif ary[mid] > target:
            right = mid - 1
        elif ary[mid] < target:
            left = mid + 1
    if ret != -1:
        while ret < len(ary) and ary[ret] == target:
            ret += 1
        ret -= 1
    return ret

def getCasesCntWhichMakesSumZero(cases, num):
    
    left = bisect_left(cases, -num)
    right = bisect_right(cases, -num)
    
    if left == -1:
        return 0
    else:
        return right - left + 1

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
cdSums = getCartasianProductSum(Cs, Ds)

answer = 0

for abSum in abSums:
    answer += getCasesCntWhichMakesSumZero(cdSums, abSum)

print(answer)