from collections import defaultdict
import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
r -= 1
c -= 1
N = 3
A = [list(map(int, input().split())) for _ in range(N)]

def transpose(ary):
    return list(map(list, zip(*ary)))

def doOperationR(ary):
    for i in range(len(ary)):
        # 빈도 수 세기
        numCnt = defaultdict(int)
        for num in ary[i]:
            if num != 0:
                numCnt[num] += 1
        
        # 관련 숫자 묶기 for 정렬
        temp = []
        for num, cnt in numCnt.items():
            temp.append((num, cnt))
        temp.sort(key=lambda x:(x[1], x[0]))

        # 새 열 만들기 
        newRow = []
        for num, cnt in temp:
            newRow.append(num)
            newRow.append(cnt)
        ary[i] = newRow

    # 최대 row 크기 찾기
    maxRowSize = 0
    for i in range(len(ary)):
        maxRowSize = max(maxRowSize, len(ary[i]))
    
    # row 크기 똑같이 맞추기
    for i in range(len(ary)):
        ary[i].extend([0 for _ in range(maxRowSize - len(ary[i]))])

    # row 크기 100이하로 유지
    dumpHorizontal(ary)

def getOperationCResult(ary):
    tAry = transpose(ary)
    doOperationR(tAry)
    dumpHorizontal(ary)
    retAry = transpose(tAry)
    return retAry

def dumpHorizontal(ary):
    targetLeftCnt = 100
    for i in range(len(ary)):
        ary[i] = ary[i][:100]

def checkAnswerable(A, r, c):
    return len(A) >= r + 1 and len(A[0]) >= c + 1

time = 0

while True:
    if time > 100:
        time = -1
        break
    if not checkAnswerable(A, r, c) or A[r][c] != k:
        if len(A) >= len(A[0]):
            doOperationR(A)
        else:
            A = getOperationCResult(A)
        
        time += 1
    elif A[r][c] == k:
        break

print(time)