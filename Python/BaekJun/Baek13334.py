import heapq
import sys
input = sys.stdin.readline

n = int(input())
tracks = list(list(map(int, input().split())) for _ in range(n))
d = int(input())

notIncludedInRangeHp = []
partIncludedInRangeHp = []
allIncludedInRangeHp = []

for track in tracks:
    track.sort()
    if (track[1] - track[0]) > d:
        continue
    heapq.heappush(notIncludedInRangeHp, (track[1], track[0]))

if not notIncludedInRangeHp:
    print(0)
    exit()

start = notIncludedInRangeHp[0][0]
end = start + d
result = 0
while partIncludedInRangeHp or notIncludedInRangeHp:
    while notIncludedInRangeHp and (start <= notIncludedInRangeHp[0][1] <= end):
        nEnd, nStart = heapq.heappop(notIncludedInRangeHp)
        heapq.heappush(partIncludedInRangeHp, (nEnd, nStart))

    while partIncludedInRangeHp and (start <= partIncludedInRangeHp[0][0] <= end) and (start <= partIncludedInRangeHp[0][1] <= end):
        nEnd, nStart = heapq.heappop(partIncludedInRangeHp)
        heapq.heappush(allIncludedInRangeHp, (nEnd, nStart))

    result = max(result, len(allIncludedInRangeHp))
    if allIncludedInRangeHp:
        heapq.heappop(allIncludedInRangeHp)
        if allIncludedInRangeHp:
            start = allIncludedInRangeHp[0][1]
            end = start + d
    elif partIncludedInRangeHp:
        start = partIncludedInRangeHp[0][1]
        end = start + d
    elif notIncludedInRangeHp:
        start = notIncludedInRangeHp[0][1]
        end = start + d

print(result)