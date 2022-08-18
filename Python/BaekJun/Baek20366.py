import math
import sys
input = sys.stdin.readline


N = int(input())
snowBalls = list(map(int, input().split()))
snowBalls.sort()

def findMinDiff(snowBalls):
    foundEquals = False
    minDiff = int(4e10)
    for i in range(N):
        for j in range(i + 1, N):
            left = i + 1
            right = N - 1
            snowManSum1 = snowBalls[i] + snowBalls[j]
            while left < right:
                if left == j:
                    left += 1
                    continue
                elif right == j:
                    right -= 1
                    continue
                
                snowManSum2 = snowBalls[left] + snowBalls[right]
                minDiff = min(minDiff, abs(snowManSum1 - snowManSum2))
                if snowManSum1 == snowManSum2:
                    return 0
                elif snowManSum1 > snowManSum2:
                    left += 1
                elif snowManSum1 < snowManSum2:
                    right -= 1
    return minDiff


print(findMinDiff(snowBalls))