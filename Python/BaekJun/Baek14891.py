import sys
input = sys.stdin.readline

# (0 == 안움직임, -1 == 반시계, 1 == 시계)
# N == 0, S == 1
# streamDir == set / 왼 == -1, 오 == 1
moveR = set([1])
moveL = set([-1])
moveLR = set([1, -1])

wheelCnt = 4
wheelEdgeCnt = 8

def getScore(wheel, wheelNum):
  if wheel[0] == 0:
    return 0
  else:
    return 2**(wheelNum - 1)

def rotateSingleWheel(wheel, rotateDir):
  wheelEdgeCnt = len(wheel)
  tempWheel = [v for v in wheel]
  if rotateDir == 1:
    wheel = wheel[-1] + wheel[:-1]
  elif rotateDir == -1:
    wheel = wheel[1:] + wheel[0]
  

def getRotateDir(myEdgeNum, counterEdgeNum, myRotateDir):
  if myEdgeNum == counterEdgeNum:
    return 0
  else:
    return 1 if 1 != myRotateDir else -1

def rotate(streamDir, rotateDir, wheelIdx, wheels):
  global moveR, moveL, moveLR
  global wheelCnt, wheelEdgeCnt
  
  if rotateDir == 0:
    return

  if moveR.issubset(streamDir):
    nextWheelIdx = wheelIdx + 1
    if 0 <= nextWheelIdx < wheelCnt:
      rightWheelRotateDir = getRotateDir(wheels[wheelIdx][2], wheels[nextWheelIdx][6], rotateDir)
      rotate(moveR, rightWheelRotateDir, nextWheelIdx, wheels)
  if moveL.issubset(streamDir):
    nextWheelIdx = wheelIdx - 1
    if 0 <= nextWheelIdx < wheelCnt:
      leftWheelRotateDir = getRotateDir(wheels[wheelIdx][6], wheels[nextWheelIdx][2], rotateDir)
      rotate(moveL, leftWheelRotateDir, nextWheelIdx, wheels)

  # 나를 회전 시킴
  rotateSingleWheel(wheels[wheelIdx], rotateDir)

wheels = []

# 입력
for _ in range(wheelCnt):
  line = input().strip()
  temp = []
  for idx in range(wheelEdgeCnt):
    temp.append(int(line[idx]))
  wheels.append(temp)

K = int(input())
commands = [list(map(int, input().split())) for _ in range(K)]

for wheelNum, rotateDir in commands:
  rotate(moveLR, rotateDir, wheelNum - 1, wheels)
  
answer = 0
for idx in range(len(wheels)):
  answer += getScore(wheels[idx], idx + 1)

print(answer)