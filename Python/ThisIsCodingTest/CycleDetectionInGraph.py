import sys
input = sys.stdin.readline

def find_parent(parent_, x):
  if parent_[x] != x:
    parent_[x] = find_parent(parent_, parent_[x])
  return parent_[x]  

def union_parent(parent_, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 입력
V, E = map(int, input().split())

parent = [i for i in range(V + 1)]


cycle = False
for _ in range(E):
  u, v = map(int, input().split())
  
  u_parent = find_parent(parent, u)
  v_parent = find_parent(parent, v)
  # 부모가 같으면 사이클 발생
  if u_parent == v_parent:
    cycle = True
    break
  # 다르면 합치기
  union_parent(parent, u, v)

if cycle:
  print("사이클 발생")
else:
  print("사이클 발생x")

