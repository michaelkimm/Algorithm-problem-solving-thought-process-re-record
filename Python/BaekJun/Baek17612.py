import heapq
from collections import deque
import sys
input = sys.stdin.readline

N, k = map(int, input().split())
customers = [list(map(int, input().split())) for _ in range(N)]
timeLefts = [0 for _ in range(k)]
queues = [deque([]) for _ in range(k)]
for i in range(N):
    appendIdx = timeLefts.index(min(timeLefts))
    timeLefts[appendIdx] += customers[i][1]
    queues[appendIdx].append(customers[i])

# init hp
hp = []
for qIdx in range(len(queues)):
    cid, cVal = queues[qIdx].popleft()
    heapq.heappush(hp, (cVal, -qIdx, cid))

result = []
while hp:
    # 감소될 시간 get
    cVal, _, _ = hp[0]

    # hp 내 모든 남은 시간 감소
    for i in range(len(hp)):
        tmpVal, tmpQIdx, tmpId = hp[i]
        tmpVal -= cVal
        hp[i] = (tmpVal, tmpQIdx, tmpId)
    
    # hp에 사람 있고, hp top이 0이면 계속 뽑기
    poppedQList = []
    while hp and hp[0][0] == 0:
        tmpVal, tmpQIdx, tmpId = heapq.heappop(hp)
        result.append(tmpId)
        poppedQList.append(tmpQIdx)
    
    # hp에서 뽑힌 사람이 속한 열에서 popoleft 후 hp 삽입
    for tmpQIdx in poppedQList:
        if queues[-tmpQIdx]:
            tmpId, tmpVal = queues[-tmpQIdx].popleft()
            heapq.heappush(hp, (tmpVal, tmpQIdx, tmpId))

answer = 0
for i, val in enumerate(result):
    answer += ((i + 1) * val)

print(answer)