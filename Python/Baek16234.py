import sys
from collections import deque

def MakeUnionBFS(si, sj):
  global country, visited, di, dj, L, R, poseCandidate
  
  total = 0
  count = 0

  queue = deque([(si, sj)])
  union = [(si, sj)]
  
  # 방문 처리
  visited[si][sj] = True
  count = 1
  total += country[si][sj]

  while queue:
    ci, cj = queue.popleft()
    for i in range(4):
      # 인접 노드들
      ni = ci + di[i]
      nj = cj + dj[i]
      # 접근 불가하면
      if not (0 <= ni < len(visited) and 0 <= nj < len(visited[0])):
        continue
      # 방문한적 있으면
      if visited[ni][nj]:
        continue
      # 조건 만족하면
      if L <= abs(country[ni][nj] - country[ci][cj]) <= R:
        # 다음 후보에 삽입
        queue.append((ni, nj))
        visited[ni][nj] = True
        count += 1
        total += country[ni][nj]
        union.append((ni, nj))

  # 평균 값 계산
  if count > 1:
    mean = total // count
    for node in union:
      country[node[0]][node[1]] = mean
      # 새로 계산된 곳 근처만 계산하면 된다.
      poseCandidate.append((node[0], node[1]))
    return True
  return False



  

# 입력
N, L, R = map(int, sys.stdin.readline().split())
country = []
for _ in range(N):
  country.append(list(map(int, sys.stdin.readline().split())))

# 초기화
visited = [[False] * N for _ in range(N)] 
poseCandidate = deque([])
for i in range(N):
  for j in range(N):
    poseCandidate.append((i, j))
populationPassedDayCount = 0

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

while True:
  size = len(poseCandidate)
  unionExist = False

  for _ in range(size):
    ci, cj = poseCandidate.popleft()
    if not visited[ci][cj]:
      if MakeUnionBFS(ci, cj):
        unionExist = True

  if not unionExist:
    break
  
  for i in range(N):
    for j in range(N):
      visited[i][j] = False
  
  populationPassedDayCount += 1

print(populationPassedDayCount)