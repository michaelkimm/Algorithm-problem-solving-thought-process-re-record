def check_id_matched(key, value):
    if len(key) != len(value):
        return False
    idx = 0
    while key[idx] == value[idx] or key[idx] == '*':
        idx += 1
        if idx == len(key):
            break
    return True if idx == len(key) else False

def get_ids_matched(banned_id, user_ids):
    matched = []
    for user_id in user_ids:
        if check_id_matched(banned_id, user_id):
            matched.append(1)
        else:
            matched.append(0)
    return matched
    
def my_dfs(ci, cj, visited, banned_id_candis, result):
    if ci != -1:    
        visited[cj] = True
    if ci + 1 == len(banned_id_candis):
        result.add(''.join(['1' if v else '0' for v in visited]))
        
    for j in range(len(visited)):
        ni = ci + 1
        nj = j
        if ni < len(banned_id_candis) and banned_id_candis[ni][nj] == 1 and not visited[nj]:
            my_dfs(ni, nj, visited, banned_id_candis, result)
    if ci != -1:
        visited[cj] = False

def solution(user_id, banned_id):
    banned_id_candis = []
    visited = [False] * len(user_id)
    for b_id in banned_id:
        ids_matched = get_ids_matched(b_id, user_id)
        banned_id_candis.append(ids_matched)
    result = set()
    my_dfs(-1, -1, visited, banned_id_candis, result)
    answer = len(result)
    return answer