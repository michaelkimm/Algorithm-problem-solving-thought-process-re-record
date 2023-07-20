import sys
input = sys.stdin.readline

def getCost(sPt, ePt):
    return abs(sPt[0] - ePt[0]) + abs(sPt[1] - ePt[1])

dist = [[2000000001 for _ in range(8)] for _ in range(8)]
si, sj = map(int, input().split())
ei, ej = map(int, input().split())
nodes = []
nodes.append((si, sj))
for idx in range(1, 4):
    psi, psj, pei, pej = map(int, input().split())
    # idx * 2 - 1
    nodes.append((psi, psj))
    # idx * 2
    nodes.append((pei, pej))

    dist[idx * 2 - 1][idx * 2] = min(10, getCost((psi, psj), (pei, pej)))
    dist[idx * 2][idx * 2 -1] = min(10, getCost((psi, psj), (pei, pej)))
nodes.append((ei, ej))

# 1-2, 3-4, 4-5,
for i in range(8):
    for j in range(8):
        dist[i][j] = min(dist[i][j], getCost(nodes[i], nodes[j]))

for k in range(8):
    for i in range(8):
        for j in range(8):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print(dist[0][7])