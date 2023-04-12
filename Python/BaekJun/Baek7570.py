import sys
input = sys.stdin.readline

class childInfo:
    def __init__(self, index, smallerNumberCnt):
        self.index = index
        self.smallserNumberCnt = smallerNumberCnt

    def __str__(self):
        return ' '.join([str(self.index), str(self.smallserNumberCnt)])    

n = int(input())
childs = list(map(int, input().split()))

lineInfoDict = dict()
for idx, child in enumerate(childs):
    if (child - 1) in lineInfoDict and lineInfoDict[child - 1].index < idx:
        lineInfoDict[child] = childInfo(idx, lineInfoDict[child - 1].smallserNumberCnt + 1) #child가 몇번째 인덱스인지, 자기 포함 앞에 몇명 있는지
    elif not((child - 1) in lineInfoDict):
        lineInfoDict[child] = childInfo(idx, 1)

maxConsequenceCnt = 0

for key in lineInfoDict.keys():
    maxConsequenceCnt = max(lineInfoDict[key].smallserNumberCnt, maxConsequenceCnt)

print(n - maxConsequenceCnt)