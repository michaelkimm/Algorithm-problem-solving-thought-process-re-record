from collections import defaultdict

N = 50
parent = [i * N + j for i in range(N) for j in range(N)]
values = [ "EMPTY" for i in range(N) for j in range(N)]

def getId(r, c):
    return r * N + c

def find_parent(idNumber):
    global parent, values
    if parent[idNumber] != idNumber:
        return find_parent(parent[idNumber])
    return idNumber

def union_find(idNumber1, idNumber2):
    global parent, values
    idNumber1 = find_parent(idNumber1)
    idNumber2 = find_parent(idNumber2)
    pIdNumber = 0
    if values[idNumber1] == "EMPTY" and values[idNumber2] != "EMPTY":
        parent[idNumber1] = idNumber2
    else:
        parent[idNumber2] = idNumber1

def solution(commands):
    global parent, values
    answer = []
    
    for command in commands:
        miniCmds = list(command.split())
        if miniCmds[0] == 'UPDATE':
            if len(miniCmds) == 4:
                cmd, r, c, value = miniCmds
                r = int(r) - 1
                c = int(c) - 1
                pId = find_parent(getId(r, c))
                values[pId] = value
            elif len(miniCmds) == 3:
                cmd, v1, v2 = miniCmds
                for i in range(N * N):
                    pId = find_parent(i)
                    if values[pId] == v1:
                        values[pId] = v2
        elif miniCmds[0] == 'MERGE':
            r1, c1, r2, c2 = map(lambda x : int(x) - 1, miniCmds[1:])
            if r1 == r2 and c1 == c2:
                continue
            union_find(getId(r1, c1), getId(r2, c2))
        elif miniCmds[0] == 'UNMERGE':
            r, c = map(lambda x : int(x) - 1, miniCmds[1:])
            targetParentId = find_parent(getId(r, c))
            parentValue = values[targetParentId]
            eraseAdvocates = []
            for i in range(N * N):
                pId = find_parent(i)
                if targetParentId == pId:
                    eraseAdvocates.append(i)
            for i in eraseAdvocates:
                values[i] = "EMPTY"
                parent[i] = i
            values[getId(r, c)] = parentValue
        elif miniCmds[0] == 'PRINT':
            r, c = map(lambda x : int(x) - 1, miniCmds[1:])
            pId = find_parent(getId(r, c))
            answer.append(values[pId])
    return answer