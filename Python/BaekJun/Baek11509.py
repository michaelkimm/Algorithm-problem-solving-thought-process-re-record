import sys
input = sys.stdin.readline

N = int(input())
balloonHeights = list(map(int, input().split()))

arrowCnt = 0
arrows = [0 for _ in range(1000000 + 2)]
for i in range(N):
    if arrows[balloonHeights[i]] == 0:
        arrowCnt += 1
        arrows[balloonHeights[i] - 1] += 1
    else:
        arrows[balloonHeights[i]] -= 1
        arrows[balloonHeights[i] - 1] += 1

print(arrowCnt)