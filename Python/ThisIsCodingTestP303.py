from collections import deque
import sys
input = sys.stdin.readline

# 입력
N = int(input())
graph = [[] for i in range(N + 1)]
entry_list = [0 for i in range(N + 1)]
time_list = [0] * (N + 1)

for node in range(1, N + 1):
  data = list(map(int, input().split()))
  time_list[node] += data[0]
  for u in data[1:-1]:
    graph[u].append(node)
    entry_list[node] += 1

q = deque()
for node in range(1, N + 1):
  if entry_list[node] == 0:
    q.append(node)

costList = [0 for i in range(N + 1)]
for node in range(1, N + 1):
  costList[node] += time_list[node]

while q:
  node = q.popleft()
  
  for v in graph[node]:
    entry_list[v] -= 1
    costList[v] = max(costList[v], costList[node] + time_list[v])
    if entry_list[v] == 0:
      q.append(v)

print("cost_list", costList)