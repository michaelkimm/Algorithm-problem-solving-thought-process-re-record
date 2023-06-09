from collections import deque
import sys
input = sys.stdin.readline

def printBelts(tops, bottoms, robots, durabilityLists = []):
    print("tops:", tops)
    print("bots:", bottoms)
    print("robots:", robots)
    print("durs:", durabilityLists)
    print("=====================")


def spinBelts(tops, bottoms, robots):
    bottoms.append(tops.pop())
    tops.appendleft(bottoms.popleft())
    # 로봇 또한 벨트와 함께 회전
    for i in range(len(robots) - 2, -1, -1):
        if robots[i]:
            robots[i + 1] = True
            robots[i] = False
        if i + 1 == len(robots) - 1 and robots[i + 1]:
            robots[i + 1] = False


def getZeroCnt(durabilityLists):
    cnt = 0
    for i in range(len(durabilityLists)):
        if durabilityLists[i] == 0:
            cnt += 1
    return cnt

def moveRobot(tops, bottoms, durabilityLists, robots):
    newZeroCnt = 0
    for robotIdx in range(len(robots) - 2, -1, -1):
        if robots[robotIdx] and not(robots[robotIdx + 1]) and durabilityLists[tops[robotIdx + 1]] >= 1:
            if robotIdx + 1 != len(robots) - 1:
                robots[robotIdx + 1] = True
            else:
                robots[robotIdx + 1] = False
            robots[robotIdx] = False
            durabilityLists[tops[robotIdx + 1]] -= 1
            if durabilityLists[tops[robotIdx + 1]] == 0:
                newZeroCnt += 1
            

    return newZeroCnt

N, K = map(int, input().split())

tops = deque([k for k in range(1, N + 1)])
bottoms = deque([k for k in range(2*N, N, -1)])
durabilityLists = list(map(int, input().split()))
durabilityLists.insert(0, -1)

zeroCnt = getZeroCnt(durabilityLists)
robots = [False for _ in range(N)]

result = 1
while (zeroCnt < K):
    spinBelts(tops, bottoms, robots)
    zeroCnt += moveRobot(tops, bottoms, durabilityLists, robots)
    if durabilityLists[tops[0]] != 0:
        robots[0] = True
        durabilityLists[tops[0]] -= 1
        if durabilityLists[tops[0]] == 0:
            zeroCnt += 1
    result += 1

print(result - 1)