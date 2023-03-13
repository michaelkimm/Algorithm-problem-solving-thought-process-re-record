import sys
input = sys.stdin.readline

N = int(input())
wasteTimes = []
values = []
for _ in range(N):
    w, v  = map(int, input().split())
    wasteTimes.append(w)
    values.append(v)

dp = [0 for _ in range(N)]

for today in range(N):
    dp[today] = max(dp[today], dp[today - 1] if today - 1 >= 0 else 0)
    endDayWithThisJob = today + wasteTimes[today] - 1
    if endDayWithThisJob >= N:
        continue
    dp[endDayWithThisJob] = max(dp[endDayWithThisJob], dp[today - 1] + values[today] if today - 1 >= 0 else values[today]) 

print(dp)