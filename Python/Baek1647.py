from errno import ESTALE
import sys
input = sys.stdin.readline

def  find_parent(parent, n):
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

N, M = map(int, input().split())
graph = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

parent = [i for i in range(N + 1)]

graph.sort()
maxIncludedLine = 0
total = 0

# 최소 스패닝 트리
for c, a, b in graph:
    if union_parent(parent, a, b):
        total += c
        maxIncludedLine = max(maxIncludedLine, c)

# 남은 간선 중 가장 크기 큰 간선 제거
print(total - maxIncludedLine)