import heapq
from collections import deque
import sys
input = sys.stdin.readline

N, k = map(int, input().split())
customers = [list(map(int, input().split())) for _ in range(N)]
timeLefts = [0 for _ in range(k)]
queues = [deque([]) for _ in range(k)]
inputHp = []
# O(KlogK)
for i in range(k):
    heapq.heappush(inputHp, (0, i))

goOutList = []
# O(NlogK)
for i in range(N):
    cId, cWaitTime = customers[i]
    # O(logK)
    totalWaitTime, appendQIdx = heapq.heappop(inputHp)
    queues[appendQIdx].append((cId, cWaitTime))
    # O(logK)
    newTotalWaitTime = totalWaitTime + cWaitTime
    heapq.heappush(inputHp, (newTotalWaitTime, appendQIdx))
    goOutList.append((newTotalWaitTime, -appendQIdx, cId))

goOutList.sort()
print(goOutList)
answer = 0
for i, val in enumerate(goOutList):
    _, _, cId = val
    answer += ((i + 1) * cId)

print(answer)