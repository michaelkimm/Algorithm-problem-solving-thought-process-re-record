import sys
input = sys.stdin.readline

# 북, 북동, 동, 남동, 남, 남서, 서, 북서
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())

graph = [[[] for _ in range(N)] for _ in range(N)]
fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r -= 1
    c -= 1
    fireballs.append((r, c, m, s, d))
    graph[r][c].append((m, s, d))


def move(fireballInfo, graph):
    r, c, m, s, d = fireballInfo
    nr = (r + s * dr[d]) % N
    nc = (c + s * dc[d]) % N
    graph[r][c].remove((m, s, d))
    graph[nr][nc].append((m, s, d))
    return (nr, nc, m, s, d)

def getFireballMassSum(fireballs):
    sum = 0
    for fireballInfo in fireballs:
        r, c, m, s, d = fireballInfo
        sum += m
    return sum

def isAlldirectionOddOrEven(directions):
    isOdds = False
    isEvens = False
    for idx, direction in enumerate(directions):
        if direction % 2 == 0:
            if isOdds:
                return False
            isEvens = True
        elif direction % 2 != 0:
            if isEvens:
                return False
            isOdds = True
    return True

def doSumAndDivideOperation(fireballs, graph):
    global N
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) < 2:
                continue
            massSum = 0
            speedSum = 0
            cnt = len(graph[i][j])
            directions = []
            for fireballInfo in graph[i][j]:
                m, s, d = fireballInfo
                massSum += m
                speedSum += s
                directions.append(d)
                
                fireballs.remove((i, j, m, s, d))
            
            # 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋
            singleMass = massSum // 5
            # 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋
            singleSpeed = speedSum // cnt
            # 방향은 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
            directions = [0, 2, 4, 6] if isAlldirectionOddOrEven(directions) else [1, 3, 5, 7]
            # 질량이 0인 파이어볼은 소멸되어 없어진다.
            newFireballs = []
            if singleMass != 0:
                newFireballs = [(singleMass, singleSpeed, d) for d in directions]
            # 새 파이어볼들로 교체
            graph[i][j] = newFireballs
            for m, s, d in newFireballs:
                fireballs.append((i, j, m, s, d))

def print2dArray(description, ary):
    print(description)
    for line in ary:
        print(line)
    print("=================")

def print1dArray(description, ary):
    print(description)
    print(ary)
    print("=================")

movementCnt = 0
while movementCnt < K:
    newFireballs = []
    for fireballInfo in fireballs:
        movedFireballInfo = move(fireballInfo, graph)
        newFireballs.append(movedFireballInfo)
    fireballs = newFireballs
    
    doSumAndDivideOperation(fireballs, graph)
    movementCnt += 1

print(getFireballMassSum(fireballs))