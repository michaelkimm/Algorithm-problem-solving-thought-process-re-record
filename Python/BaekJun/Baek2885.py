import math
import sys
input = sys.stdin.readline

K = int(input())

powerOfTwoSet = set([int(math.pow(2, p)) for p in range(21)])

def getSmallestNeededSize(k):
    result = 0
    while k % 2 == 0 and k != 0:
        k = k >> 1
        result += 1
    return int(math.pow(2, result))

def getChopNeededCnt(originalSize, pieceSize):
    result = 0
    while originalSize > pieceSize:
        originalSize = originalSize >> 1
        result += 1
    return result    

originalSize = int(math.pow(2, len(format(K, 'b')))) if K not in powerOfTwoSet else K
smallestNeededSize = getSmallestNeededSize(K)
answer = getChopNeededCnt(originalSize, smallestNeededSize)
print(originalSize, answer)