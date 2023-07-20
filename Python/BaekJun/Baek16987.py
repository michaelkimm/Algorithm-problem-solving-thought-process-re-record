from itertools import product
import sys
input = sys.stdin.readline

N = int(input())
durabilities = []
weights = []
for _ in range(N):
    d, w = map(int, input().split())
    durabilities.append(d)
    weights.append(w)

answer = 0

def recursive(onHandIdx, brokenCnt):
    global N, answer
    if onHandIdx >= N:
        answer = max(answer, brokenCnt)
        return
    
    for hitIdx in range(N):
        if onHandIdx == hitIdx:
            continue
        beforeHitIdxDur = durabilities[hitIdx]
        beforeOnHandDur = durabilities[onHandIdx]
        beforeBrokenCnt = brokenCnt
        if durabilities[onHandIdx] > 0 and durabilities[hitIdx] > 0:
            durabilities[onHandIdx] -= weights[hitIdx]
            durabilities[hitIdx] -= weights[onHandIdx]
            if durabilities[onHandIdx] <= 0:
                brokenCnt += 1
            if durabilities[hitIdx] <= 0:
                brokenCnt += 1

        recursive(onHandIdx + 1, brokenCnt)

        durabilities[onHandIdx] = beforeOnHandDur
        durabilities[hitIdx] = beforeHitIdxDur
        brokenCnt = beforeBrokenCnt

recursive(0, 0)
print(answer)