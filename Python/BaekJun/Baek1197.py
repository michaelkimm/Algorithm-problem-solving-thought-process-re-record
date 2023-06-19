import sys
input = sys.stdin.readline


def findParent(parent, u):
    if parent[u] != u:
        parent[u] = findParent(parent, parent[u])
    return parent[u]

def unionParent(parent, u, v):
    a = findParent(parent, u)
    b = findParent(parent, v)
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
graph = []
parent = [i for i in range(V + 1)]
for _ in range(E):
    u, v, c = map(int, input().split())
    graph.append((c, u, v))

graph.sort()


answer = 0
for c, u, v in graph:
    if findParent(parent, u) == findParent(parent, v):
        continue
    answer += c
    unionParent(parent, u, v)

print(answer)