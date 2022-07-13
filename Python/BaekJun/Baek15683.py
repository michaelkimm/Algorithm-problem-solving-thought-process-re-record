import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

cases = [
  [],
  [[0], [1], [2], [3]],
  [[0,1], [2,3]],
  [[0,3], [0,2], [1,2], [1,3]],
  [[0,1,2], [0,1,3], [0,2,3], [1,2,3]],
  [[0,1,2,3]]
        ]

# 입력
N, M = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))

# CCTV 위치 찾기
# get : [(CCTV번호, i, j)]
cctvInfos = []
for i in range(N):
  for j in range(M):
    if graph[i][j] != 0 and graph[i][j] != 6:
      cctvInfos.append((graph[i][j], i, j))

# from : [[(CCTV번호, 회전 정보, i, j)...],[],[]...]
def activateCctv(cctvNum, rotateInfos, pose, graph):
  ci, cj = pose
  for rotateInfo in rotateInfos:
    ni, nj = ci + di[rotateInfo], cj + dj[rotateInfo]
    while (0 <= ni < N and 0 <= nj < M) and graph[ni][nj] != 6:
      graph[ni][nj] = '#'
      ni, nj = ni + di[rotateInfo], nj + dj[rotateInfo]

def getBlindSpotCnt(graph):
  ret = 0
  for i in range(len(graph)):
    for j in range(len(graph[0])):
      if graph[i][j] == 0:
        ret += 1
  return ret

def getMinBlindSpotCnt(cctvInfos, graph):
  global cases
  if not cctvInfos:
    return getBlindSpotCnt(graph)
    
  cctvNum, ci, cj = cctvInfos.pop()

  ret = int(1e21)
  # 나머지 케이스 계산
  for case in cases[cctvNum]:
    # cctv 작동
    g = [[graph[i][j] for j in range(M)] for i in range(N)]
    activateCctv(cctvNum, case, (ci, cj), g)
    tempCCTVInfos = [v for v in cctvInfos]
    ret = min(ret, getMinBlindSpotCnt(tempCCTVInfos, g))

  return ret

print(getMinBlindSpotCnt(cctvInfos, graph))
