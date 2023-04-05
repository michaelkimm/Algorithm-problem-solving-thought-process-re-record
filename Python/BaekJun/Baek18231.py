import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

K = int(input())
destroyedCities = set(list(map(int, input().split())))
bombedCities = set()
destoryedConfirmed = set()
for destroyedCity in destroyedCities:
    # if destroyedCity in destoryedConfirmed:
        # continue
    flag = True
    for v in graph[destroyedCity]:
        if not(v in destroyedCities):
            flag = False
            break
    if flag:
        bombedCities.add(destroyedCity)
        destoryedConfirmed.add(destroyedCity)
        for v in graph[destroyedCity]:
            destoryedConfirmed.add(v)

if len(destoryedConfirmed) != K:
    print(-1)
else:
    print(len(bombedCities))
    print(' '.join(str(v) for v in sorted(list(bombedCities))))