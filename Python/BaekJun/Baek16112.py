import sys
input = sys.stdin.readline

n, k = map(int, input().split())
stoneValues = sorted(list(map(int, input().split())))

answer = 0

activatedCnt = 0
for i in range(n):
    # if not activatedStoneDict.keys():
    #     activatedStoneDict[i] = stoneValues[i]
    if activatedCnt < k:
        # 기존에 활성화된 돌에 경험치 추가
        answer += (stoneValues[i] * activatedCnt)
        activatedCnt += 1
    else:
        # 기존에 활성화된 돌에 경험치 추가
        answer += (stoneValues[i] * activatedCnt)

print(answer)