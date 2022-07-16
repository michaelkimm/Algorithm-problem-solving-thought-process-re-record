import re
import sys
input = sys.stdin.readline

# 동 = 0, 북 = 1, 서 = 2, 남 = 3

def rotateCW(pts, cnt, start, end):
    # {0 -1;1 0}
    ret = set([v for v in pts])
    for _ in range(cnt):
        start = (-start[1], start[0])
        end = (-end[1], end[0])
        tempRet = set([])
        for pt in ret:
            x = pt[0]
            y = pt[1]
            tempRet.add((-y, x))
        ret = set([v for v in tempRet])
    return ret, start, end

# (0,0) 기준 회전
def defaultRotatePts(pts, rotationDir, start, end):
    if rotationDir == 1:
        return rotateCW(pts, 3, start, end)
    elif rotationDir == 2:
        return rotateCW(pts, 2, start, end)
    elif rotationDir == 3:
        return rotateCW(pts, 1, start, end)
    else:
        return pts, start, end

def movePts(pts, dx, dy, start, end):
    ret = set([])
    for pt in pts:
        x = pt[0]
        y = pt[1]
        ret.add((x + dx, y + dy))
    return ret, (start[0] + dx, start[1] + dy), (end[0] + dx, end[1] + dy)

def getNextGeneration(prevGeneration, start, end):
    tempPrevGeneration = set([v for v in prevGeneration])
    orgStart = start
    orgEnd = end

    # 끝점을 (0,0으로 이동). 끝점(0, 0)을 시작 점이라고 생각.
    tempPrevGeneration, end, start = movePts(tempPrevGeneration, -end[0], -end[1], start, end)

    # 회전
    tempPrevGeneration, start, end = rotateCW(tempPrevGeneration, 1, start, end)

    # 시작점을 이전 끝점으로 이동
    tempPrevGeneration, start, end = movePts(tempPrevGeneration, orgEnd[0], orgEnd[1], start, end)

    tempPrevGeneration = tempPrevGeneration.union(prevGeneration)

    return tempPrevGeneration, orgStart, end

def getDefaultDragonCurve(g):
    # (0,0)에서 동쪽으로 g세대 동안 성장
    start = (0, 0)
    end = (1, 0)
    dragonCurve = [start, end]
    for _ in range(g):
        dragonCurve, start, end = getNextGeneration(dragonCurve, start, end)
    return dragonCurve, start, end

def getDragonCurve(x, y, d, g):
    # (0,0)에서 동쪽으로 g세대 동안 성장
    dragonCurve, start, end = getDefaultDragonCurve(g)

    # d 방향으로 회전
    dragonCurve, start, end = defaultRotatePts(dragonCurve, d, start ,end)

    # (x,y) 위치로 이동
    dragonCurve, start, end = movePts(dragonCurve, x, y, start, end)
    return dragonCurve, start, end

def rectInDragons(rectInfo, dragons):
    ret = True
    for pt in rectInfo:
        if not pt in dragons:
            ret = False
            break 
    return ret

N = int(input())
totalDragons = set([])
for _ in range(N):
    x, y, d, g = map(int, input().split())
    newDragonCurve, start, end = getDragonCurve(x, y, d, g)
    totalDragons = totalDragons.union(newDragonCurve)

# 겹치는 단위 사각형 개수 (0, 0) ~ (99, 99)
answer = 0
for x in range(100):
    for y in range(100):
        rectInfo = [(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)]
        if rectInDragons(rectInfo, totalDragons):
            answer += 1

print(answer)