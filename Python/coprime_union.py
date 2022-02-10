import sys
input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent_, a, b):
  a = find_parent(parent_, a)
  b = find_parent(parent_, b)
  if a < b:
    parent_[b] = a
  else:
    parent_[a] = b

# 입력
V, E = map(int, input().split())

parent = [0] * (V + 1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, V + 1):
  parent[i] = i

for _ in range(E):
  u, v = map(int, input().split())
  union_parent(parent, u, v)


for node in range(1, V + 1):
  print(find_parent(parent, node), end=' ')
print("")



print(parent)

