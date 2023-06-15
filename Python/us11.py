import bisect
import math
import sys
input = sys.stdin.readline

N = int(input())

powerOfTwoNums = [1]
element = 2
while powerOfTwoNums[-1] < N:
    powerOfTwoNums.append(powerOfTwoNums[-1] * element)

def getPowerOf2ElementSameOrSmallerThan(n):
    bIdx = bisect.bisect_left(powerOfTwoNums, n)
    if int(math.pow(2, bIdx)) == n:
        return bIdx
    else:
        return bIdx - 1

def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    k = getPowerOf2ElementSameOrSmallerThan(n)

    return int(math.pow(3, k)) + solution(n - int(math.pow(2, k)))

print(solution(N))