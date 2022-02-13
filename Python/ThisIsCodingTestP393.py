import sys
input = sys.stdin.readline

def find_parent(parent, n):
  if parent[n] != n:
    parent[n] = find_parent(parent, parent[n])
  return parent[n]
  
def union_parent(parent, u, v):
  u = find_parent(parent, u)
  v = find_parent(parent, v)
  if u < v:
    parent[v] = u
  else:
    parent[u] = v

# 입력
N, M = map(int, input().split())
nxn = []
for _ in range(N):
  nxn.append(list(map(int, input().split())))

travel_plan = list(map(int, input().split()))

parent = [i for i in range(N + 1)]

for i in range(N):
  for j in range(i, N):
    if nxn[i][j] == 1:
      union_parent(parent, i + 1, j + 1)

result = True
first_city = travel_plan[0]
for idx in range(1, len(travel_plan)):
  if find_parent(parent, first_city) != find_parent(parent, travel_plan[idx]):
    result = False
    break

if result:
  print("YES")
else:
  print("NO")