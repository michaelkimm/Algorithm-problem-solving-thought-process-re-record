import math
import sys
input = sys.stdin.readline

def unionFind(parent, x):
    if parent[x] != x:
        parent[x] = unionFind(parent, parent[x])
    return parent[x]

def merge(parent, pt1, pt2):
    a = unionFind(parent, pt1)
    b = unionFind(parent, pt2)
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
stars = [(0, 0) for _ in range(n + 1)]
for i in range(1, n + 1):
    x, y = map(float, input().split())
    stars[i] = (x, y)


edges = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        pt1 = stars[i]
        pt2 = stars[j]
        c = math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)
        edges.append((c, i, j))
parent = [i for i in range(n + 1)]

edges.sort()

answer = 0
for c, u, v in edges:
    if unionFind(parent, u) == unionFind(parent, v):
        continue
    answer += c
    merge(parent, u, v)

print(format(answer, ".2f"))