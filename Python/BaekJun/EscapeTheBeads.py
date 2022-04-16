from collections import deque
import sys

def move_ball(ci, cj, di, dj, toy_map_, ball_type):
  ni, nj = move(ci, cj, di, dj, toy_map_)
  toy_map_ = toy_map_.replace(ball_type, '.')
  if not (ni == oi and nj == oj):
    toy_map_ = toy_map_[:ni * M + nj] + ball_type + toy_map_[ni * M + nj + 1:]
  return ni, nj, toy_map_

def move(ci, cj, di, dj, toy_map):
  ni = ci + di
  nj = cj + dj
  if toy_map[ni * M + nj] == '.':
    return move(ni, nj, di, dj, toy_map)
  elif (toy_map[ni * M + nj] == '#' or toy_map[ni * M + nj] == 'B' or toy_map[ni * M + nj] == 'R'):
    return ci, cj
  elif toy_map[ni * M + nj] == 'O':
    return ni, nj

# 입력
input = sys.stdin.readline
N, M = map(int, input().split())
toy_map = ''
for _ in range(N):
  toy_map += input().strip()

# 초기화
ri, rj, bi, bj, oi, oj = 0, 0, 0, 0, 0, 0
for i in range(N):
  for j in range(M):
    if toy_map[i * M + j] == 'B':
      bi, bj = i, j
    elif toy_map[i * M + j] == 'R':
      ri, rj = i, j
    elif toy_map[i * M + j] == 'O':
      oi, oj = i, j

# BFS 풀이
# 간선: 상하좌우 움직이기
# 노드: (빨간 구슬 위치, 파란 구슬 위치, 맵 상태)로 정의
cost = 0
answer = -1
q = deque([(ri, rj, bi, bj, toy_map, cost)])
visited = set()
while q:
  ri, rj, bi, bj, toy_map, cost = q.popleft()

  # 확인한 경우인지 검사
  if (ri, rj, bi, bj, toy_map) in visited:
    continue
  visited.add((ri, rj, bi, bj, toy_map))

  # 파랑 구슬이 구멍에 빠짐
  if bi == oi and bj == oj:
    continue
  # 빨간 구슬이 구멍에 빠짐
  if ri == oi and rj == oj:
    answer = cost
    break
  # 코스트 10이상은 패스
  if cost >= 10:
    continue
    
  # 상하좌우 움직이기
  for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    # 기울어질 방향쪽에 더 가까운 구슬 부터 굴리기
    if (di == -1 and ri <= bi) or (di == 1 and ri >= bi) or (dj == -1 and rj <= bj) or (dj == 1 and rj >= bj):
      # 빨강
      tmp_toy_map = toy_map
      nri, nrj, tmp_toy_map = move_ball(ri, rj, di, dj, tmp_toy_map, 'R')
      # 파랑 
      nbi, nbj, tmp_toy_map = move_ball(bi, bj, di, dj, tmp_toy_map, 'B')
      q.append((nri, nrj, nbi, nbj, tmp_toy_map, cost + 1))

    if (di == -1 and ri > bi) or (di == 1 and ri < bi) or (dj == -1 and rj > bj) or (dj == 1 and rj < bj):
      # 파랑 
      tmp_toy_map = toy_map
      nbi, nbj, tmp_toy_map = move_ball(bi, bj, di, dj, tmp_toy_map, 'B')
      # 빨강
      nri, nrj, tmp_toy_map = move_ball(ri, rj, di, dj, tmp_toy_map, 'R')
      q.append((nri, nrj, nbi, nbj, tmp_toy_map, cost + 1))

if answer > 10:
  answer = -1

print(answer)