from itertools import product
import sys
input = sys.stdin.readline

N = int(input())
eggInfos = [list(map(int, input().split())) for _ in range(N)]

def hit(hitIdx, onHandIdx, eggInfos):
    onHandDur, onHandWt = eggInfos[onHandIdx]
    hitDur, hitWt = eggInfos[hitIdx]
    if onHandDur <= 0 or hitDur <= 0:
        return 0
    onHandDur -= hitWt
    hitDur -= onHandWt
    eggInfos[onHandIdx] = (onHandDur, onHandWt)
    eggInfos[hitIdx] = (hitDur, hitWt)
    brokeCnt = 0
    if onHandDur <= 0:
        brokeCnt += 1
    if hitDur <= 0:
        brokeCnt += 1
    return brokeCnt
    
# print(list(product([v for v in range(N)], repeat=N)))
answer = 0
for case in product([v for v in range(N)], repeat=N):
    onHandIdx = 0
    caseAnswer = 0
    caseEggInfo = [v for v in eggInfos]
    for hitIdx in case:
        if hitIdx == onHandIdx:
            continue
        caseAnswer += hit(hitIdx, onHandIdx, caseEggInfo)
        onHandIdx += 1
    answer = max(answer, caseAnswer)
print(answer)