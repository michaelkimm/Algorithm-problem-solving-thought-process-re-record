import sys
input = sys.stdin.readline

N = int(input())
reservations = [list(map(int, input().split())) for _ in range(N)]

reservations.sort(key=lambda x: (x[1], x[0]))

result = 0
startableTime = 0
for startTime, endTime in reservations:
    if startTime >= startableTime:
        result += 1
        startableTime = endTime

print(result)