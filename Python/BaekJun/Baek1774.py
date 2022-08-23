from itertools import combinations
import math
import sys
input = sys.stdin.readline

def findParent(parent, u):
    if parent[u] != u:
        parent[u] = findParent(parent, parent[u])
    return parent[u]

def unionParent(parent, uIndex, vIndex):
    uParentIndex = findParent(parent, uIndex)
    vParentIndex = findParent(parent, vIndex)
    if uParentIndex < vParentIndex:
        parent[vParentIndex] = uParentIndex
    else:
        parent[uParentIndex] = vParentIndex

def checkIfMakesCycle(parent, uIndex, vIndex):
    uParentIndex = findParent(parent, uIndex)
    vParentIndex = findParent(parent, vIndex)
    return uParentIndex == vParentIndex



N, M = map(int, input().split())
godposes = [list(map(int, input().split())) for _ in range(N)]

def getLength(p1, p2):
    return sqrt(pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[0]), 2))

def getLengthSum(lines):
    global godposes
    ret = 0
    for p1Index, p2Index in lines:
        p1 = godposes[p1Index]
        p2 = godposes[p2Index]
        ret += getLength(p1, p2)
    return ret

def getUnLinkedLineWithLength(unLinkedLines):
    global godposes
    ret = []
    for p1Index, p2Index in unLinkedLines:
        p1 = godposes[p1Index]
        p2 = godposes[p2Index]
        length = getLength(p1, p2)
        ret.append((p1, p2, length))
    ret.sort(reverse=True, key=lambda x:x[2])
    return ret

lines = []         
for _ in range(M):
    p1Index, p2Index = map(int, input().split())
    lines.append((p1Index - 1, p2Index - 1))
lines.sort()

unLinkedLines = set(sorted(list(combinations(range(N), 2))))
# 이미 있는 포인트 삭제
for lineInfo in lines:
    unLinkedLines.remove(lineInfo)
unLinkedLines = getUnLinkedLineWithLength(unLinkedLines)

# 이미 연결된 간선 정보를 parent에 업데이트
parent = [i for i in range(N)]
for p1Index, p2Index in lines:
    unionParent(parent, p1Index, p2Index)

# 이미 있는 포인트 간 거리 구하기
answer = getLengthSum(lines)
while unLinkedLines:
    uIndex, vIndex, length = unLinkedLines.pop()

    if checkIfMakesCycle(parent, uIndex, vIndex):
        continue
    else:
        unionParent(parent, uIndex, vIndex)
        answer += length

print(answer)



# 현재 까지 구현 사항은 이론 상 모두 끝냄.
# 내일부터 차례 차례 함수 하나 하나 잘 구현됐는지 검증해보자.