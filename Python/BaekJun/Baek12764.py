import heapq
import sys
input = sys.stdin.readline


N = int(input())
users = [list(map(int, input().split())) for _ in range(N)]
users.sort()

comUsedRecords = []
availComHp = []
comUsing = []
computerIdx = -1
maxCnt = 0

for startTime, endTIme in users:
    while comUsing and comUsing[0][0] < startTime:
        _, reuseComIdx = heapq.heappop(comUsing)
        heapq.heappush(availComHp, reuseComIdx)
    if not availComHp:
        computerIdx += 1
        comUsedRecords.append(1)
        heapq.heappush(comUsing, (endTIme, computerIdx))
    else:
        reuseComIdx = heapq.heappop(availComHp)
        heapq.heappush(comUsing, (endTIme, reuseComIdx))
        comUsedRecords[reuseComIdx] += 1
    maxCnt = max(maxCnt, len(comUsing))

print(len(comUsedRecords))
for i in range(len(comUsedRecords)):
    print(comUsedRecords[i], end=' ')