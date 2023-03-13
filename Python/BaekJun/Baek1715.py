import heapq
import sys
input = sys.stdin.readline

N = int(input())
hp = []
for _ in range(N):
    heapq.heappush(hp, (int(input())))


def getMComparedCnt(hp):
    result = 0
    if len(hp) == 1:
        return result
    while len(hp) >= 2:

        cardSet1 = heapq.heappop(hp)
        cardSet2 = heapq.heappop(hp)
        newCardSet = cardSet1 + cardSet2
        result += newCardSet
        heapq.heappush(hp, newCardSet)
    
    return result

print(getMComparedCnt(hp))