from collections import deque
import sys
input = sys.stdin.readline

def getNewBriges(bridges):
  return set([v for v in bridges])

def checkTargetOutOfMap(curPose):
  global N, H
  if curPose[0] >= H + 2 or curPose[1] >= N + 1 or curPose[0] <= 0 or curPose[1] <= 0:
    return True
  else:
    return False

def checkTargetMatched(startPose, curPose):
  global H
  if (H + 1, startPose[1]) == curPose:
    return True
  else:
    return False

def getNextStartNode(curPose):
  newPose = (1, curPose[1] + 1)
  if checkTargetOutOfMap(newPose):
    return (-1, -1)
  else:
    return newPose

def adjacentBridgeExist(curPose, curBridges):
  return (curPose[0], curPose[1] - 1) in curBridges or (curPose[0], curPose[1] + 1) in curBridges
                        
def moveRight(curPose):
  return (curPose[0], curPose[1] + 1)

def moveLeft(curPose):
  return (curPose[0], curPose[1] - 1)

def moveDown(curPose):
  return (curPose[0] + 1, curPose[1])

def postProcessBfs(nextStartPose, nextPose, visited, q, addedBridgeCnt, matchedCnt, curHorizontalBridges, crossedHorizontalBridges, newHorBridge = (-1, -1)):
  if checkTargetOutOfMap(nextPose):
    return
  newHorizontalBridges = getNewBriges(curHorizontalBridges)
  if newHorBridge != (-1, -1):
    newHorizontalBridges.add(newHorBridge)
    addedBridgeCnt += 1
    
  if (nextStartPose, nextPose, tuple(newHorizontalBridges)) in visited:
    return

  newCrossedHorizontalBridges = getNewBriges(crossedHorizontalBridges)
  newCrossedHorizontalBridges.add
  visited.add((nextStartPose, nextPose, tuple(newHorizontalBridges)))
  q.append((nextStartPose, nextPose, newHorizontalBridges, newCrossedHorizontalBridges, addedBridgeCnt, matchedCnt))
  return

def rightAvailableToGo():
  return

def crossedBridgeRightBefore(curPose, curHorizontalBridges):
  return curPose in curHorizontalBridges or (curPose[0], curPose[1] - 1) in curHorizontalBridges

def bfs(horizontalBridges):
  global N
  # 1번에서 시작
  startPose = (1, 1)
  curPose = startPose
  matchedCnt = 0
  curHorizontalBridges = getNewBriges(horizontalBridges)
  crossedHorizontalBridges = set([])
  curNode = (startPose, curPose, curHorizontalBridges, 0, matchedCnt)  # i, j, curHorizontalBridges, addedBridgeCnt, matchCnt
  visited = set([(startPose, curPose, tuple(curHorizontalBridges))])
  q = deque([curNode])
  availableRet = []
  
  while q:
    startPose, curPose, curHorizontalBridges, addedBridgeCnt, matchedCnt = q.popleft()
    leftPose = (curPose[0], curPose[1] - 1)
    print("startPose:", startPose)
    print("curPose:", curPose)
    print("curHorizontalBridges:", curHorizontalBridges)
    print("addedBridgeCnt:", addedBridgeCnt)
    print("================================")
    

    # 끝 도달
    if checkTargetMatched(startPose, curPose):
      matchedCnt += 1
      print("Target Matched! curPose:", curPose)
      print("matchedCnt:", matchedCnt)
      print("===")
      
      nextPose = getNextStartNode(curPose)
      nextStartPose = nextPose
      if nextPose == (-1, -1):
        if matchedCnt == N:
          print("Found one! curPose:", curPose)
          availableRet.append(addedBridgeCnt)
          print("availableRet:", availableRet)
          print("***")
        continue
        
      postProcessBfs(nextStartPose, nextPose, visited, q, addedBridgeCnt, matchedCnt, curHorizontalBridges, crossedHorizontalBridges)
      continue
    
    # 간선
    # 우측 놓여져 있으면 무조건 가기
    if curPose in curHorizontalBridges:
      nextPose = moveRight(curPose)
      postProcessBfs(startPose, nextPose, visited, q, addedBridgeCnt, matchedCnt, curHorizontalBridges, crossedHorizontalBridges)
      continue
    # 좌측이 놓여져 있으면 무조건 가기
    if leftPose in curHorizontalBridges:
      nextPose = moveLeft(curPose)
      postProcessBfs(startPose, nextPose, visited, q, addedBridgeCnt, matchedCnt, curHorizontalBridges, crossedHorizontalBridges)
      continue
      
    # 좌우측 갈 수 있으면 가기
    if addedBridgeCnt <= 2:
      if not crossedBridgeRightBefore(curPose, curHorizontalBridges):
        # 좌측
        nextPose = moveLeft(curPose)
        postProcessBfs(startPose, nextPose, visited, q, addedBridgeCnt, matchedCnt, curHorizontalBridges, crossedHorizontalBridges, leftPose)
        # 우측
        nextPose = moveRight(curPose)
        postProcessBfs(startPose, nextPose, visited, q, addedBridgeCnt, matchedCnt, curHorizontalBridges, crossedHorizontalBridges, curPose)

    # 내려가기
    nextPose = moveDown(curPose)
    postProcessBfs(startPose, nextPose, visited, q, addedBridgeCnt, matchedCnt, curHorizontalBridges, crossedHorizontalBridges)
      
  return -1 if not availableRet else min(availableRet)

# 입력
N, M, H = map(int, input().split())

# 초기화
horizontalBridges = set([])

# 입력
for _ in range(M):
  a, b = map(int, input().split())
  horizontalBridges.add((a, b))

# 노드: 사다리 시작 노드, 위치, 사다리 상태
# 간선
  # 우측 다리
    # 다리 3개 초과x
    # 우측 건너기(이미 다리가 놓여 있어서 가는 경우, 갈 수 있을 때 선택하는 경우(연속된 두다리x))
  # 아래 건너기
  # 도착하면 위에서 새로 시작
# 탈출 조건: 맨밑인데 숫자 다른 경우, 끝까지 도착한 경우
print(bfs(horizontalBridges))



