# 2차원 배열 회전 함수
def Turn2DArrayCW(ary):
  rowCnt = len(ary)
  colCnt = len(ary[0])
  result = []
  for colIdx in range(colCnt):
    newRow = []
    for rowIdx in range(rowCnt-1, -1, -1):
      newRow.append(ary[rowIdx][colIdx])
    result.append(newRow)
  return result
  
def Turn2DArrayCWs(ary, rotateCnt):
  result = ary
  for _ in range(rotateCnt):
    result = Turn2DArrayCW(result)
  return result

def Flip2DArray(ary_):
  result = []
  for i in range(len(ary_)):
    temp = []
    for j in range(len(ary_[0]) - 1, -1, -1):
      temp.append(ary_[i][j])
    result.append(temp)
  return result

def CheckKernelInArray(kernel_, array_, si, sj):
  tetRowSize = len(kernel_)
  tetColSize = len(kernel_[0])
  if si + tetRowSize - 1 > len(array_) - 1:
    return False
  elif sj + tetColSize - 1 > len(array_[0]) - 1:
    return False
  
  return True

def CalculateConv(kernel_, ary_, si, sj):
  result = 0
  for i in range(len(kernel_)):
    for j in range(len(kernel_[0])):
      result += kernel_[i][j] * ary_[si + i][sj + j]
  return result

def dfs(curNode, visited, graph):
  visited[curNode] = True
  print("v:", curNode)

  for adjNode in graph[curNode]:
    if not visited[adjNode]:
      dfs(adjNode, visited, graph)

from collections import deque

def bfs(start, visited, graph):
  queue = deque([start])
  visited[start] = True

  while queue:
    curNode = queue.popleft()
    print("v:", curNode)

    for adjNode in graph[curNode]:
      if not visited[adjNode]:
        visited[adjNode] = True
        queue.append(adjNode)

        
def array1Dto2D(ary, n, m):
  result = []
  for i in range(n):
    tmp = []
    for j in range(m):
      tmp.append(ary[i * m + j])
    result.append(tmp)
  return result