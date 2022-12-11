import sys

number_id = 0

def dfs(cur_node, is_root, graph, discovered, is_articulation_pt):
    global number_id
    number_id += 1
    discovered[cur_node] = number_id
    result = discovered[cur_node]
    child = 0
    for next_node in graph[cur_node]:
        
        if not discovered[next_node]:
            # DFS에서 탐색이 완료되지 않은 정점이면, 새로운 트리의 시작입니다. 
            child += 1
            prev = dfs(next_node, False, graph, discovered, is_articulation_pt)
            
            # WHEN : cur_node가 시작 노드가 아닐 때
            # cur_node에서 child 노드들이 cur_node를 거치지 않고 cur_node보다 빠른 방문 번호(number_id)를 가진 정점으로 갈수 없다면 단절점임.
            if not is_root and prev >= discovered[cur_node]:
                is_articulation_pt[cur_node] = True
            result = min(result, prev)
        else:
            # 이미 DFS에서 탐색이 완료된 정점이면, 현재 정점의 number_id(방문 순서)와 탐색이 완료된 정점의 number_id(방문 순서) 중 최소 값을 찾습니다.
            result = min(result, discovered[next_node])

    # WHEN : cur_node가 시작 노드일 시
    # 자식 수가 2개 이상이면 단절점이다.
    if is_root and child > 1:
        is_articulation_pt[cur_node] = True
    
    return result

def main():
    global number_id
    while True:

        print("Give me the node count smaller than 21")
        v = int(input().strip())
        if v < 0:
            print("====================== end ======================")
            break
        adjacent_matrix = []
        graph = [[] for _ in range(v + 1)]
        discovered = [0 for _ in range(v + 1)]
        is_articulation_pt = [False for _ in range(v + 1)]
        ap_lst = []

        for i in range(1, v + 1):
            adjacent_info = list(map(int, input().split()))
            adjacent_matrix.append(adjacent_info)
            for j, val in enumerate(adjacent_info):
                if val == 0:
                    continue
                graph[i].append(j + 1)

        start_node = int(input().strip())
        dfs(start_node, True, graph, discovered, is_articulation_pt)

        for i in range(1, v+1):
            if is_articulation_pt[i]:
                ap_lst.append(i)

        print("")
        print("1. Input graph in adjacency matrix style")
        for line in adjacent_matrix:
            print(line)
        print("")
        print("2. Num of all node :", [v for v in range(1, v + 1)])
        print("3. Low value of all nodes :", [v for i, v in enumerate(discovered) if i != 0])
        print("4. Articulation points with their Num and Low values")
        for node in ap_lst:
            print("AP Num :", node, "\tLow value :", discovered[node])
        
        number_id = 0
        print("============================================")
    
if __name__ == "__main__":
    main()