from collections import deque
import heapq
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
employeeInfos = []
workDays = []
hurryWeights = []
for _ in range(N):
    d, h = map(int, input().split())
    workDays.append(d)
    hurryWeights.append(h)

# workday, hurryWeight, lineIdx, 긴 줄에서의 idx
queues = [deque() for _ in range(M)]
for i in range(N):
    lineIdx = i % M
    queues[lineIdx].append((workDays[i], hurryWeights[i], lineIdx, i))

cnt = 0
toiletUsedPersonIdx = -1
frontHp = []
for i in range(M):
    if queues[i]:
        # m개 줄에서 사람 빼기
        workday, hurryWeight, lineIdx, personIdx = queues[i].popleft()
        # 선두만 가지고 hp 생성
        heapq.heappush(frontHp, (-workday, -hurryWeight, lineIdx, personIdx))
while frontHp:
    # 화장실 사용할 사람 pop
    workday, hurryWeight, lineIdx, personIdx = heapq.heappop(frontHp)
    toiletUsedPersonIdx = personIdx
    if toiletUsedPersonIdx == K:
        break
    cnt += 1

    # 뽑았던 줄에 사람 있으면 heap에 넣기
    if queues[lineIdx]:
        workday, hurryWeight, lineIdx, personIdx = queues[lineIdx].popleft()
        heapq.heappush(frontHp, (-workday, -hurryWeight, lineIdx, personIdx))

print(cnt)