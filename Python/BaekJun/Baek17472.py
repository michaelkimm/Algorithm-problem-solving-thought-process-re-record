import sys
input = sys.stdin.readline

# 동서남북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def findParent(parent, u):
    if parent[u] != u:
        parent[u] = findParent(parent, parent[u])
    return parent[u]

def unionParent(parent, u, v):
    uParent = findParent(parent, u)
    vParent = findParent(parent, v)
    if uParent < vParent:
        parent[vParent] = uParent
    else:
        parent[uParent] = vParent

def checkIfMakesCycle(parent, u, v):
    uParent = findParent(parent, u)
    vParent = findParent(parent, v)
    return uParent == vParent

def InitializeGraph(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 1:
                graph[i][j] = -1

def getNodeInfos(graph):
    global di, dj
    N = len(graph)
    M = len(graph[0])

    # nodes = list(set((1,1), (1,2)..), set(), set(), ..)
    nodes = []
    # make graph 
    # 0 0 0 0 0 0 1 1
    # 2 2 0 0 0 0 1 1
    # 2 2 0 0 0 0 0 0
    # 2 2 0 0 0 3 3 0
    # 0 0 0 0 0 3 3 0
    # 0 0 0 0 0 0 0 0
    # 4 4 4 4 4 4 4 4

    visited = [[False for _ in range(M)] for _ in range(N)]
    ID = 1
    for i in range(N):
        for j in range(M):
            
            if visited[i][j] or graph[i][j] == 0:
                continue

            newNode = set()
            stack = [(i, j)]
            visited[i][j] = True
            
            while stack:
                ci, cj = stack.pop()
                graph[ci][cj] = ID
                newNode.add((ci, cj))

                for dirIndex in range(4):
                    ni = ci + di[dirIndex]
                    nj = cj + dj[dirIndex]
                    if not (0 <= ni < N and 0 <= nj < M):
                        continue
                    if graph[ni][nj] == -1:
                        visited[ni][nj] = True
                        stack.append((ni, nj))
            ID += 1
            nodes.append(newNode)
    
    return nodes


def getNodeIndex(graph, pt):
    return graph[pt[0]][pt[1]]

def getLineInfos(nodes, graph):
    global di, dj
    N = len(graph)
    M = len(graph[0])
    # lines = [(node1ID, node2ID, length), ...]
    lines = []
    for nodeInfo in nodes:
        # nodeInfo = set((1,1), (1,2)..)
        for pt in nodeInfo:
            # pt = (1, 1)
            # 동서남북 4칸 이상 같은 방향으로 바다 만으로 건넜을 때 다른 노드 나오면 lines에 추가
            ci, cj = pt
            for dirIndex in range(4): 
                cnt = 1
                canMakeLine = False
                ni, nj = 0, 0
                while True:
                    ni = ci + di[dirIndex] * cnt
                    nj = cj + dj[dirIndex] * cnt
                    if not (0 <= ni < N and 0 <= nj < M):
                        break
                    # 같은 색이면
                    if graph[ni][nj] == graph[ci][cj]:
                        break
                    if graph[ni][nj] != 0 and graph[ni][nj] != graph[ci][cj]:
                        canMakeLine = True
                        break
                    cnt += 1
                if canMakeLine and cnt >= 3:
                    n1Id = getNodeIndex(graph, pt)
                    n2Id = getNodeIndex(graph, (ni, nj))
                    lines.append((n1Id, n2Id, cnt - 1))
    return list(set(lines))

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

InitializeGraph(graph)

# node = list(set((1,1), (1,2)..), set(), set(), ..)
nodes = getNodeInfos(graph)

lines = getLineInfos(nodes, graph)
lines.sort(reverse=True, key=lambda x:x[2])
parent = [i for i in range(len(nodes) + 1)]

lengthSum = 0
connectedCnt = 0
# 크루스칼 알고리즘
while lines:
    node1ID, node2ID, length = lines.pop()
    if checkIfMakesCycle(parent, node1ID, node2ID):
        continue
    else:
        unionParent(parent, node1ID, node2ID)
        lengthSum += length
        connectedCnt += 1

if connectedCnt == (len(nodes) - 1):
    print(lengthSum)
else:
    print(-1)