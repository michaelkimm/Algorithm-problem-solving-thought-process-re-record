import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def findParent(parent, u):
    if u != parent[u]:
        parent[u] = findParent(parent, parent[u])
    return parent[u]

def unionParent(parent, u, v):
    uParent = findParent(parent, u)
    vParent = findParent(parent, v)

    if uParent < vParent:
        parent[vParent] = uParent
    else:
        parent[uParent] = vParent

def checkIfItMakesCycle(parent, u, v):
    uParent = findParent(parent, u)
    vParent = findParent(parent, v)

    return uParent == vParent

lines = []
parent = [i for i in range(N)]
for u in range(N):
    for v in range(u + 1, N):
        val = graph[u][v]
        lines.append((val, u, v))
lines.sort(reverse=True)

minSum = 0
while lines:
    val, u, v = lines.pop()
    if checkIfItMakesCycle(parent, u, v):
        continue
    else:
        unionParent(parent, u, v)
        minSum += val

print(minSum)
