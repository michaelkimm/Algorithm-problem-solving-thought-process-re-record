import sys
input = sys.stdin.readline

def find_parent(parent, n):
  if parent[n] != n:
    parent[n] = find_parent(parent, parent[n])
  return parent[n]

def union_parent(parent, u, v):
  if find_parent(parent, u) == find_parent(parent, v):
    return False

  u = find_parent(parent, u)
  v = find_parent(parent, v)
  if u < v:
    parent[v] = u
  else:
    parent[u] = v
  return True

N = int(input())
xList = []
yList = []
zList = []
parent = [i for i in range(N + 1)]
for i in range(1, N + 1):
  x, y, z = map(int, input().split())
  xList.append((x, i))
  yList.append((y, i))
  zList.append((z, i))

xList.sort()
yList.sort()
zList.sort()

lineList = []
for idx in range(N):
  if idx + 1 > len(xList) - 1:
    break

  lineList.append((abs(xList[idx][0] - xList[idx + 1][0]), xList[idx][1], xList[idx + 1][1]))
  lineList.append((abs(yList[idx][0] - yList[idx + 1][0]), yList[idx][1], yList[idx + 1][1]))
  lineList.append((abs(zList[idx][0] - zList[idx + 1][0]), zList[idx][1], zList[idx + 1][1]))

lineList.sort()

total = 0

for cost, u, v in lineList:
  if union_parent(parent, u, v):
    total += cost

print(total)