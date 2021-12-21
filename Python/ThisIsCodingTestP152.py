from collections import deque

# 입력 받기
# 미로 크기
N, M = map(int, input().split())

#start = list(map(int, input().spilt()))
#end = list(map(int, input().spilt()))

# 미로
graph = []
for _ in range(N):
  graph.append(list(map(int, input())))

start = [0, 0]
end = [N - 1, M - 1]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs (si, sj, end_, graph_):
  global dx, dy
  
  # 큐 생성
  queue = deque([si * len(graph_) + sj])

  # 방문
  graph_[si][sj] = 1
  
  while queue:
    # 꺼내기
    curPos = queue.popleft()
    ci = int(curPos / len(graph_[0]))
    cj = curPos % len(graph_[0])
    print("curV:", ci, cj)
    # 도착하면 out
    if (ci == end_[0] and cj == end_[1]):
      print("ci,cj:", ci, cj)
      break

    # 인접 노드들
    for i in range(4):
      ni = int(curPos / len(graph_[0])) + dy[i]
      nj = curPos % len(graph_[0]) + dx[i]

      # 범위 밖이면 그만
      if (ni < 0 or ni > len(graph_) - 1 or nj < 0 or nj > len(graph_[0]) - 1):
        continue

      # 방문 안했으면
      #print("ni,nj:", ni, nj, "   si,sj:", si, sj)
      if graph_[ni][nj] == 1 and not(ni == si and nj == sj):
        # 삽입 
        queue.append(ni * len(graph_[0]) + nj)
        # 방문
        graph_[ni][nj] = graph_[ci][cj] + 1
        #print("graph_[ni][nj]: ", graph_[ni][nj])
  return graph_



print(bfs(start[0], start[1], end, graph))