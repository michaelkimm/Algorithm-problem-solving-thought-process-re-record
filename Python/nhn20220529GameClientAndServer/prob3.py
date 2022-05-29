from collections import deque 

def solution(maze, queries):
  answer = []

  for query in queries:
    qs = query.split(" ")
    start = (int(qs[0]) - 1, int(qs[1]) - 1)
    end = (int(qs[2]) - 1, int(qs[3]) - 1)
    passable = qs[4]

    answer.append(bfs(maze, start, end, passable))
    # break
  return answer


def bfs(maze, start, end, passable):
  # 동서남북
  di = [0, 0, 1, -1]
  dj = [-1, 1, 0, 0]
  visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
  cost = 1
  q = deque([(start, cost)])
  arrived = False
  while q:
    curSite, curCost = q.popleft()
    # print(curSite, "cost:", curCost)
    
    if curSite == end:
      cost = curCost
      arrived = True
      break
    for idx in range(4):
      ni = curSite[0] + di[idx]
      nj = curSite[1] + dj[idx]
      if 0 > ni or ni >= len(maze) or nj < 0 or nj >= len(maze[0]):
        continue
      if not maze[ni][nj] in passable:
        continue
      # print((ni, nj))
      if visited[ni][nj]:
        continue
      q.append(((ni, nj), curCost + 1))
      visited[ni][nj] = True
      
  if arrived:
    return cost
  else:
    return -1


m = ["AAAAA", "AABBB", "CAEFG", "AAEFF"]
qs = ["1 1 1 5 AF", "1 1 4 5 AF", "2 1 4 5 FAE", "1 5 4 5 ABF", "1 1 4 1 A"]
print(solution(m, qs))