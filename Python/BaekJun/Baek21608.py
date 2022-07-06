import sys
input = sys.stdin.readline

def getAdjacentLikeCnt(graph, ci, cj, likes):
  result = 0  
  for idx in range(4):
    ni = ci + di[idx]
    nj = cj + dj[idx]
    if not (0 <= ni < len(graph) and 0 <= nj < len(graph)):
      continue
    if likes.count(graph[ni][nj]) > 0:
      result += 1
  return result

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

satisfiedAmount = [0, 1, 10, 100, 1000]

totalSatisfiedAmount = 0

N = int(input())
n = N * N
graph = [[0 for _ in range(N)] for _ in range(N)]

likeInfo = [[0, 0, 0, 0] for _ in range(N * N + 1)]

while n > 0:
  n -= 1
  me, l1, l2, l3, l4 = map(int, input().split())
  likeInfo[me] = [l1, l2, l3, l4]
  
  likeCnt = 0  
  emptyCnt = 0
  
  ri, rj = 0, 0
  candidates = []
  for ci in range(N):
    for cj in range(N):
      if graph[ci][cj] != 0:
        continue

      likeCnt = 0  
      emptyCnt = 0
      for idx in range(4):
        ni = ci + di[idx]
        nj = cj + dj[idx]
        if not (0 <= ni < N and 0 <= nj < N):
          continue
        if graph[ni][nj] in likeInfo[me]:
          likeCnt += 1
        if graph[ni][nj] == 0:
          emptyCnt += 1
        candidates.append((likeCnt, emptyCnt, ci, cj))
      
  candidates.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
  graph[candidates[0][2]][candidates[0][3]] = me

answer = 0
for i in range(N):
  for j in range(N):
    cnt = getAdjacentLikeCnt(graph, i, j, likeInfo[graph[i][j]])
    answer += satisfiedAmount[cnt]

print(answer)
  

      
        


