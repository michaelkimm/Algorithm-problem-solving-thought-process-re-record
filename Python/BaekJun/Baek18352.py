from collections import deque

N, M, K, X = map(int, input().split())
adjList = [[] for _ in range(N + 1)]

for _ in range(M):
  n1, n2 = map(int, input().split())
  adjList[n1].append(n2)

# 변수 초기화
resultList = []
visitedList = [-1] * (N + 1)

def bfs(start, adjList_, visited_):
  global resultList, K

  # 큐 초기화
  queue = deque([start])

  # 방문 처리
  visited_[start] = 0

  while queue:
    # 하나 뽑기
    curNode = queue.popleft()

    # 인접노드들
    for adjNode in adjList_[curNode]:
      # 방문한적 없다면
      if visited_[adjNode] == -1:
        # 큐에 담기
        queue.append(adjNode)
        # 방문 처리
        visited_[adjNode] = visited_[curNode] + 1
        if visited_[adjNode] == K:
          resultList.append(adjNode)

bfs(X, adjList, visitedList)

if resultList:
  resultList.sort()
  for node in resultList:
    print(node)
else:
  print(-1)

