import sys
input = sys.stdin.readline

N = int(input())
entryCarIDs = [input().strip() for _ in range(N)]
outCarIDs = [input().strip() for _ in range(N)]

entryRanking = dict()
outRanking = dict()
for i in range(N):
    entryCarID = entryCarIDs[i]
    entryRanking[entryCarID] = i

answer = 0
for i in range(N):
    for j in range(i + 1, N):
        if entryRanking[outCarIDs[i]] > entryRanking[outCarIDs[j]]:
            answer += 1
            break

print(answer)