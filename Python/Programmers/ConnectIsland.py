INF = int(1e9)

def find_parent(n, parent):
    if parent[n] != n:
        parent[n] = find_parent(parent[n], parent)
    return parent[n]

def union_parent(u, v, parent):
    u = find_parent(u, parent)
    v = find_parent(v, parent)
    if u == v:
        return False
    if u < v:
        parent[v] = u
    else:
        parent[u] = v
    
    return True

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    
    parent = [node for node in range(n + 1)]
    answer = 0
    for u, v, c in costs:
        if union_parent(u, v, parent):
            answer += c
    return answer