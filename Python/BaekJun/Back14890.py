import sys
input = sys.stdin.readline

def getTranspose(ary):
  return [list(row) for row in zip(*ary)]

def getVeritcalCrossable(graph, N, L):
  return getHorizontalCrossable(getTranspose(graph), N, L)

def getHorizontalCrossable(graph, N, L):
  answer = 0
  for i in range(N):
    block_cnt = 0
    prev_height = -1
    crossable = True
    for j in range(N):
      d = graph[i][j] - prev_height
      # 평지
      if prev_height == -1 or d == 0:
        prev_height = graph[i][j]
        block_cnt += 1
        continue
      # 이전 칸과 2칸 이상 차이
      if abs(d) >= 2:
        crossable = False
        break
        
      # 올라갈 경우
      if d == 1:
        if block_cnt < L:
          crossable = False
          break
        else:
          block_cnt = 1
          prev_height = graph[i][j]
          continue
      # 내려올 경우
      if d == -1:
        block_remainings = N - j
        # 남은 블럭이 L보다 적은 경우
        if block_remainings < L:
          crossable = False
          break
        else:
          predictable_blocks = set(graph[i][j:j + L])
          # 현재~앞 L개 블럭 내 숫자가 한개만 존재
          if len(predictable_blocks) == 1:
            block_cnt = -(L - 1)
            prev_height = graph[i][j]
            continue
          else:
            crossable = False
            break
    
    if crossable:
      answer += 1
  return answer

N, L = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))

answer = getHorizontalCrossable(graph, N, L) + getVeritcalCrossable(graph, N, L)
print(answer)