def dfs(n, graph, start_node, visited, ignore_line):
    count = 0
    stack = [start_node]
    visited[start_node] = True
    while stack:
        node = stack.pop()
        count += 1
        for next_n in graph[node]:
            if (node, next_n) == ignore_line:
                continue
            if not visited[next_n]:
                visited[node] = True
                stack.append(next_n)
    return count

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for n1, n2 in wires:
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    min_abs = int(1e10)
    for n1, n2 in wires:
        visited = [False] * (n + 1)
        ignore_line = (n1, n2)
        c1 = dfs(n, graph, n1, visited, ignore_line)
        c2 = dfs(n, graph, n2, visited, ignore_line)
        min_abs = min(min_abs, abs(c1 - c2))
        
    answer = min_abs
    return answer


# =========================================== #