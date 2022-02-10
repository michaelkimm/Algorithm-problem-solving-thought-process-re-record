import sys
input = sys.stdin.readline

def find_parent(parent_, n_):
  if parent_[n_] != n_:
    parent_[n_] = find_parent(parent_, parent[n_])
  return parent_[n_]

def union_parent(parent_, u_, v_):
  if find_parent(parent_, u_) == find_parent(parent_, v_):
    return False
  
  u_parent = find_parent(parent_, u_)
  v_parent = find_parent(parent_, v_)
  if u_parent < v_parent:
    parent_[v_parent] = u_parent
  else:
    parent_[u_parent] = v_parent

  return True

V, E = map(int, input().split())
graph = []
for _ in range(E):
  u, v, d = map(int, input().split())
  graph.append((u, v, d))

graph.sort(key=lambda x: x[2])

total = 0

parent = [i for i in range(V + 1)]

for u, v, d in graph:
  if union_parent(parent, u, v):
    total += d

print(total)