from itertools import combinations
def make_paper(w, h):
    paper = [['.'] * w for _ in range(h)]
    return paper

def solution(line):
    intersectPts = set()
    INF = int(1e10)
    xMax, xMin = -INF, INF
    yMax, yMin = -INF, INF
    for line1, line2 in combinations(line, 2):
        A, B, E = line1[0], line1[1], line1[2]
        C, D, F = line2[0], line2[1], line2[2]
        
        parent = A * D - B * C
        if parent == 0:
            continue
            
        xSon = B * F - E * D
        ySon = E * C - A * F
        x = xSon / parent
        y = ySon / parent

        if x != int(x) or y != int(y):
            continue
        x = int(x)
        y = int(y)
        xMax, xMin = max(xMax, x), min(xMin, x)
        yMax, yMin = max(yMax, y), min(yMin, y)

        intersectPts.add((x, y))
            
    w = xMax - xMin + 1
    h = yMax - yMin + 1
    paper = make_paper(w, h)
    for pt in intersectPts:
        paper[yMax-pt[1]][pt[0]-xMin] = '*'
    
    return [''.join(line) for line in paper]