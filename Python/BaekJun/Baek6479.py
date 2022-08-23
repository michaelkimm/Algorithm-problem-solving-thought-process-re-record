import sys
input = sys.stdin.readline


def union_find(parent, u):
    if parent[u] != u:
        parent[u] = union_find(parent, parent[u])
    return parent[u]

def unionParent(parent, u, v):
    uParent = union_find(parent, u)
    vParent = union_find(parent, v)
    if uParent < vParent:
        parent[vParent] = uParent
    else:
        parent[uParent] = vParent

def checkIfMakesCycle(parent, u, v):
    uParent = union_find(parent, u)
    vParent = union_find(parent, v)
    return uParent == vParent

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    parent = [i for i in range(m)]

    graph.sort(reverse = True, key=lambda x:x[2])

    answer = 0
    while graph:
        x, y, v = graph.pop()
        if checkIfMakesCycle(parent, x, y):
            answer += v
            continue
        else:
            unionParent(parent, x, y)

    print(answer)
