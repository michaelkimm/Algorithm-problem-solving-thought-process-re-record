import sys
input = sys.stdin.readline

def find_parent(parent, n):
    if parent[n] != n:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]

def union_parent(parent, u, v):
    u = find_parent(parent, u)
    v = find_parent(parent, v)
    if (u < v):
        parent[v] = u
    else:
        parent[u] = v

def check_union(parent, u, v):
    return find_parent(parent, u) == find_parent(parent, v)

N, M = map(int, input().split())

results = []

parent = [i for i in range(N + 1)]

for _ in range(M):
    judge, u, v = map(int, input().split())
    if judge == 0:
        # 합치기
        union_parent(parent, u, v)
    else:
        # 평가
        if check_union(parent, u, v):
            result = "YES"
        else:
            result = "NO"
        results.append(result)

for result in results:
  print(result)