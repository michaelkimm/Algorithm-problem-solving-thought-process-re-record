from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cache = set()
    time = 0
    q = deque([])
    for city in cities:
        city = city.lower()
        if city in cache:
            time += 1
            q.remove(city)
            q.append(city)
            continue
        time += 5
        if len(q) <= cacheSize:
            if len(q) == cacheSize:
              popped_city = q.popleft()
              cache.remove(popped_city)
            q.append(city)
            cache.add(city)
        
    answer = time
    return answer