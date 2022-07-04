# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def getSiteOfPose(i, j):
  return max(i, j)

def getNextPose(cur_i, cur_j, direction):
  next_i, next_j = cur_i + di[direction], cur_j + dj[direction]
  return next_i, next_j

def getNextPosWithAvailList(cur_site_avail_list, next_site_avail_list, direction):
  # 현재 지역 먼저
  if cur_site_avail_list[direction] != (-1, -1):
    return cur_site_avail_list[direction]
  for dirIdx in range(4):
    if cur_site_avail_list[dirIdx] != (-1, -1):
      return cur_site_avail_list[dirIdx]
  # 다음 지역
  if next_site_avail_list[direction] != (-1, -1):
    return next_site_avail_list[direction]
  for dirIdx in range(4):
    if next_site_avail_list[dirIdx] != (-1, -1):
      return next_site_avail_list[dirIdx]
   
  return -1, -1
  

def solution(n, horizontal):
  
  answer = [[0 for _ in range(n)] for _ in range(n)]
  num = 1
  ci, cj = 0, 0
  cur_site = 0
  direction = 2
  target_num = n * n

  if horizontal:
    direction = 0
  else:
    direction = 2

  cur_site_avail_list = [(-1, -1) for _ in range(4)]
  next_site_avail_list = [(-1, -1) for _ in range(4)]
  cur_site_avail_list[direction] = (ci, cj)
  
  while num <= target_num:
    ci, cj = getNextPosWithAvailList(cur_site_avail_list, next_site_avail_list, direction)
    answer[ci][cj] = num
    num += 1

    # 초기화
    cur_site_avail_list = [(-1, -1) for _ in range(4)]
    next_site_avail_list = [(-1, -1) for _ in range(4)]
    
    for dirIdx in range(4):
      ni, nj = getNextPose(ci, cj, dirIdx)
      if not (0 <= ni < n and 0 <= nj < n):
        continue
      if answer[ni][nj] != 0:
        continue
      if getSiteOfPose(ci, cj) == getSiteOfPose(ni, nj):
        cur_site_avail_list[dirIdx] = (ni, nj)
      else:
        next_site_avail_list[dirIdx] = (ni, nj)
  return answer

n= 10
horizontal = False
for line in solution(n, horizontal):
  print(line)