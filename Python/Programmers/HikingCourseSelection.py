import heapq

def solution(n, paths, gates, summits):
    
    graph = [[] for _ in range(n + 1)]
    for u, v, weight in paths:
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    summits = set(summits)
    hp = []
    for gate in gates:
        heapq.heappush(hp, (0, gate))
    INF = int(1e10)
    intensities = [INF] * (n + 1)
    
    while hp:
        intensity, curNum = heapq.heappop(hp)
        if curNum in summits or intensities[curNum] < intensity:
            continue
        for v, weight in graph[curNum]:
            newIntensity  = max(intensity, weight)
            if newIntensity < intensities[v]:
                intensities[v] = newIntensity
                heapq.heappush(hp, (newIntensity, v))
    ret = []
    for summit in summits:
        ret.append([summit, intensities[summit]])
    ret.sort(key=lambda x:(x[1], x[0]))
    return ret[0]