# 북,북서,서,남서,남,남동,동,북동
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(graph, ci, cj, visited):
    result = 0 if len(visited) == 1 else 1
    spreaded = False
    for dirIdx in range(8):
        ni = ci + di[dirIdx]
        nj = cj + dj[dirIdx]
        if not (0 <= ni < len(graph) and 0 <= nj < len(graph[0])):
            continue
        if (ni, nj) in visited:
            continue
        if graph[ni][nj] == 0:
            continue
        newVisited = set([v for v in visited])
        newVisited.add((ni, nj))
        result += dfs(graph, ni, nj, newVisited)
        spreaded = True

    if spreaded:
        return result
    else:
        if len(visited) == 1:
            return 0
        else:
            return 1


def solution(콜):
    answer = 0
    for i in range(len(콜)):
        for j in range(len(phone[0])):
            if phone[i][j] == 0:
                continue
            visited = set([(i, j)])
            availablePasswordCnt = dfs(phone, i, j, visited)
            answer += availablePasswordCnt

    return answer