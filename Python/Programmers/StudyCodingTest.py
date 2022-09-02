import heapq

def getMaxCop(problems):
    problems.sort(key=lambda x:x[1])
    return problems[-1][1]

def getMaxAlp(problems):
    problems.sort()
    return problems[-1][0]

def getUnneededFiltered(problems):
    # alpReq과 copReq의 합이 cost보다 작으면 제외
    ret = []
    for alpReq, copReq, alpRwd, copRwd, cost in problems:
        if (alpRwd + copRwd) < cost:
            continue
        ret.append([alpReq, copReq, alpRwd, copRwd, cost])
    return ret

def change2DarrayToTupleList(problems):
    ret = []
    for alpReq, copReq, alpRwd, copRwd, cost in problems:
        ret.append((alpReq, copReq, alpRwd, copRwd, cost))
    return ret

def solution(alp, cop, problems):
    
    # 1초 소모하여 알고력1 or 코딩력1
    problems.append([0, 0, 0, 1, 1])
    problems.append([0, 0, 1, 0, 1])
    maxAlp = getMaxAlp(problems)
    maxCop = getMaxCop(problems)
    problems = change2DarrayToTupleList(problems)
    # problems = getUnneededFiltered(problems)
    problems = list(set(problems))
    
    if alp >= maxAlp and cop >= maxCop:
        return 0
    
    curNode = (0, alp, cop)
    hp = [curNode]
    visited = set([])
    answer = -1
    while hp:
        curNode = heapq.heappop(hp)
        time, curAlp, curCop = curNode
        
        if curNode in visited:
            continue
        visited.add(curNode)
        
        if curAlp >= maxAlp and curCop >= maxCop:
            answer = time
            break
        # 간선
        # problems
        for alpReq, copReq, alpRwd, copRwd, cost in problems:
            if alpRwd == 0 and copRwd == 0:
                continue
            if curAlp >= alpReq and curCop >= copReq:
                heapq.heappush(hp, (time + cost, curAlp + alpRwd, curCop + copRwd))
    
    return answer


# =====================================================================

import heapq

def getMaxCop(problems):
    problems.sort(key=lambda x:x[1])
    return problems[-1][1]

def getMaxAlp(problems):
    problems.sort()
    return problems[-1][0]

def solution(alp, cop, problems):
    problems.append([0, 0, 0, 1, 1])
    problems.append([0, 0, 1, 0, 1])
    maxAlp = max(alp, getMaxAlp(problems))
    maxCop = max(cop, getMaxCop(problems))
    
    INF = int(1e10)
    hp = [(0, alp, cop)]
    distance = [INF] *(150*150 + 150 + 1)
    distance[alp * 150 + cop] = 0
    answer = -1
    while hp:
        curNode = heapq.heappop(hp)
        dist, curAlp, curCop = curNode
        if distance[curAlp * 150 + curCop] < dist:
            continue
        if curAlp >= maxAlp and curCop >= maxCop:
            answer = dist
            break
        # 간선
        for alpReq, copReq, alpRwd, copRwd, cost in problems:
            if not (curAlp >= alpReq and curCop >= copReq):
                continue
            nextAlp = min(maxAlp, curAlp + alpRwd)
            nextCop = min(maxCop, curCop + copRwd)
            nextCost = cost + dist
            if distance[nextAlp * 150 + nextCop] > nextCost:
                distance[nextAlp * 150 + nextCop] = nextCost
                heapq.heappush(hp, (nextCost, nextAlp, nextCop))
    
    return answer