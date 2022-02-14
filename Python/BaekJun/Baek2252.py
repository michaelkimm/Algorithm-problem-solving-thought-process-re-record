from collections import deque
import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
entry_cnt = [0] * (N + 1)
for _ in range(M):
    # a가 B 앞에 서야함, b->a
    a, b = map(int, input().split())
    graph[b].append(a)
    entry_cnt[a] += 1

q = deque()
result = []
# 시작 지점 초기화
for node in range(1, N + 1):
    if entry_cnt[node] == 0:
        q.appendleft(node)

while q:
    node = q.popleft()
    result.append(node)
    for v in graph[node]:
        entry_cnt[v] -= 1
        if entry_cnt[v] == 0:
            q.appendleft(v)

result.reverse()
for node in result:
    print(node, end=' ')

