def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_parent(parent, u, v):
    u = find_parent(parent, u)
    v = find_parent(parent, v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v

def solution(n, computers):
    parent = [node for node in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union_parent(parent, i, j)
                
    for i in range(n):
        parent[i] = find_parent(parent, i)
        
    parent_set = set(parent)
    return len(parent_set)

# ====================================================== #

def dfs(cur_node, visited, computers, parent, color):
    visited[cur_node] = True
    parent[cur_node] = color
    
    for next_node in range(len(computers)):
        if computers[cur_node][next_node] == 0 or visited[next_node] or next_node == cur_node:
            continue
        dfs(next_node, visited, computers, parent, color)
        

def solution(n, computers):
    visited = [False for i in range(n)]
    parent = [-1 for i in range(n)]
    for node in range(n):
        if not visited[node]:
            dfs(node, visited, computers, parent, node)
    answer_set = set(parent)
    return len(answer_set)

# ====================================================== #


def dfs(start_node, visited, computers):
    stack = [start_node]
    while len(stack) > 0:
        node = stack.pop()
        visited[node] = True
        
        for next_node in range(len(computers)):
            if computers[node][next_node] == 0 or visited[next_node]:
                continue
            stack.append(next_node)
        

def solution(n, computers):
    visited = [False for i in range(n)]
    
    answer = 0
    for node in range(n):
        if not visited[node]:
            answer += 1
            dfs(node, visited, computers)
    return answer