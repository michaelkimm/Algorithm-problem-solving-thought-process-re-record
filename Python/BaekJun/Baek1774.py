from itertools import combinations
import math
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
godposes = [list(map(int, input().split())) for _ in range(N)]


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

def getLength(p1, p2):
    return math.sqrt(math.pow((p1[0] - p2[0]), 2) + math.pow((p1[1] - p2[1]), 2))

def getUnLinkedLineWithLength(unLinkedLines):
    global godposes
    ret = []
    for p1Index, p2Index in unLinkedLines:
        p1 = godposes[p1Index]
        p2 = godposes[p2Index]
        length = getLength(p1, p2)
        ret.append((p1Index, p2Index, length))
    ret.sort(reverse=True, key=lambda x:x[2])
    return ret

lines = []         
for _ in range(M):
    p1Index, p2Index = map(int, input().split())
    lines.append((p1Index - 1, p2Index - 1))

unLinkedLines = set(list(combinations(range(N), 2)))

# 이미 있는 포인트 삭제
for lineInfo in lines:
    if lineInfo in unLinkedLines:
        unLinkedLines.remove(lineInfo)

# (p1Index, p2Index, 길이)로 변환
unLinkedLines = getUnLinkedLineWithLength(unLinkedLines)

# 이미 연결된 간선 정보를 parent에 업데이트
parent = [i for i in range(N)]
for p1Index, p2Index in lines:
    unionParent(parent, p1Index, p2Index)

# 이미 있는 포인트 간 거리 구하기
answer = 0
while unLinkedLines:
    uIndex, vIndex, length = unLinkedLines.pop()

    if checkIfMakesCycle(parent, uIndex, vIndex):
        continue
    else:
        unionParent(parent, uIndex, vIndex)
        answer += length

print('%.2f'%answer)