import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = list(map(int, input().split()))

if N == 1:
    print(1)
    exit()

hp = []
for i in range(K):
    heapq.heappush(hp, (-items[i], i))

result = []
flag = True
tmp = []
while hp:
    cntInMinus, itemIdx = heapq.heappop(hp)
    result.append(itemIdx + 1)

    if len(result) >= 2 and result[-1] == result[-2]:
        flag = False
        break

    if tmp:
        prev = tmp.pop()
        if prev[0] < 0:
            heapq.heappush(hp, prev)
    tmp.append((cntInMinus + 1, itemIdx))

if tmp:
    for _ in range(-tmp[0][0]):
        result.append(tmp[0][1] + 1)

if (not flag) or result[-1] == result[-2]:
    print(-1)
else:
    print(' '.join(str(v) for v in result))