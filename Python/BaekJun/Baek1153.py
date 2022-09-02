# from itertools import 
import sys
input = sys.stdin.readline

N = int(input())

def getPrimeNumbers(N):
    ret = []
    isPrimeNumber = [False, False] + [True] * (N - 1)
    for num in range(2, N + 1):
        if isPrimeNumber[num]:
            ret.append(num)
            for multipliedNum in range(2 * num, N + 1, num):
                isPrimeNumber[multipliedNum] = False

    return ret

print(getPrimeNumbers(N))