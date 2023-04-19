from collections import deque
import sys
input = sys.stdin.readline

# 북동남서 = 0,1,2,3
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

class Dice:
    def __init__(self, left, right, front, back, up, down):
        self.ci = 0
        self.cj = 0
        self.left = left
        self.right = right
        self.front = front
        self.back = back
        self.up = up
        self.down = down
        self.dirIdx = 1
    
    def __str__(self):
        return ''.join(["ci:", str(self.ci), " cj:", str(self.cj), " dirIdx:", str(self.dirIdx), " left: ", str(self.left), " right:", str(self.right), " front:", str(self.front), " back:", str(self.back), " up:", str(self.up), " down:", str(self.down) ])

    def checkMovable(self, N, M):
        ni = self.ci + di[self.dirIdx]
        nj = self.cj + dj[self.dirIdx]
        if not (0 <= ni < N and 0 <= nj < M):
            return False
        return True

    def movePose(self):
        self.ci = self.ci + di[self.dirIdx]
        self.cj = self.cj + dj[self.dirIdx]

    def roll(self):
        tmpFront = self.front
        tmpBack = self.back
        tmpLeft = self.left
        tmpRight = self.right
        tmpUp = self.up
        tmpDown = self.down
        if self.dirIdx == 1:
            # 동쪽
            # 동->밑, 밑->서, 서->위, 위->동
            self.down = tmpRight
            self.left = tmpDown
            self.up = tmpLeft
            self.right = tmpUp
        elif self.dirIdx == 3:
            # 서쪽
            # 위->서, 서->밑, 밑->동, 동->위
            self.down = tmpLeft
            self.left = tmpUp
            self.up = tmpRight
            self.right = tmpDown
        elif self.dirIdx == 2:
            # 남쪽
            # 위->뒤, 뒤->밑, 밑->앞, 앞->위
            self.back = tmpUp
            self.down = tmpBack
            self.front = tmpDown
            self.up = tmpFront
        elif self.dirIdx == 0:
            # 북쪽
            # 위->앞, 앞->밑, 밑->뒤, 뒤->위
            self.back = tmpDown
            self.down = tmpFront
            self.front = tmpUp
            self.up = tmpBack
        
        self.movePose()
    
    def changeDir(self, dirIdx):
        self.dirIdx = dirIdx

    def flipDir(self):
        self.dirIdx = (self.dirIdx + 2) % 4

    def spinCW(self):
        self.dirIdx = (self.dirIdx + 1) % 4

    def spinCCW(self):
        self.dirIdx = (self.dirIdx + 3) % 4

def getPoint(dice, graph):
    global di, dj
    N, M = len(graph), len(graph[0])
    visited = set()
    target = graph[dice.ci][dice.cj]
    result = graph[dice.ci][dice.cj]
    start = (dice.ci, dice.cj)
    q = deque([start])
    visited.add(start)
    while q:
        ci, cj = q.popleft()
        for dirIdx in range(4):
            ni = ci + di[dirIdx]
            nj = cj + dj[dirIdx]
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if graph[ni][nj] != target:
                continue
            if (ni, nj) in visited:
                continue
            visited.add((ni, nj))
            result += target
            q.append((ni, nj))
    return result
            
def moveDiceWithRule(dice, graph):
    point = 0
    N = len(graph)
    M = len(graph[0])
    # 주사위 굴리기
    if not dice.checkMovable(N, M):
        dice.flipDir()
    dice.roll()        

    # 점수 획득
    point = getPoint(dice, graph)

    # 이동 방향 결정
    A = dice.down
    B = graph[dice.ci][dice.cj]
    if A > B:
        dice.spinCW()
    elif A < B:
        dice.spinCCW()

    return point


dice = Dice(4, 3, 2, 5, 1, 6)
N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

answer = 0
while K > 0:
    answer += moveDiceWithRule(dice, graph)
    K -= 1

print(answer)