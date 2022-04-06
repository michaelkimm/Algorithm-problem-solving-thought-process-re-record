import sys


def front_circuit(graph, parent, ary):
    ary.append(parent)
    for n in graph[parent]:
        front_circuit(graph, n, ary)
    return
def back_circuit(graph, parent, ary):
    for n in graph[parent]:
        back_circuit(graph, n, ary)
    ary.append(parent)

def make_graph(nodes, graph):
    # print(nodes)
    if not nodes:
        return -1
    # 부모 노드 찾기
    parent_id, px, py = max(nodes, key=lambda x:x[2])
    parent_idx = nodes.index((parent_id, px, py))
    # 부모노드 양쪽으로 뻗기
    l = make_graph(nodes[:parent_idx], graph)
    if l != -1:
        graph[parent_id].append(l)
    r = make_graph(nodes[parent_idx + 1:], graph)
    if r != -1:
        graph[parent_id].append(r)
    return parent_id

def solution(nodeinfo):
    limit_number = 15000
    sys.setrecursionlimit(limit_number)

    # y 값이 가장 큰 노드가 루트 노드
    nodes = [(i + 1, pt[0], pt[1]) for i, pt in enumerate(nodeinfo)]
    x_sorted = sorted(nodes, key=lambda x: x[1])
    graph = [[] for _ in range(len(nodes) + 1)]
    root_id = make_graph(x_sorted, graph)

    # 전위, 후위 순회
    front = []
    back = []
    front_circuit(graph, root_id, front)
    back_circuit(graph, root_id, back)
    
    answer = [front, back]
    return answer