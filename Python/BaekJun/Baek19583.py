from collections import defaultdict
import sys
input = sys.stdin.readline

def strClockToMin(strClock):
    hour, minute = map(int, strClock.split(':'))
    return hour * 60 + minute


S, E, Q = map(strClockToMin, input().split())
chatBeforeStartRecord = defaultdict(list)
chatEToQtRecord = defaultdict(list)
while True:
    try:
        time, name = input().split()
        timeInMin = strClockToMin(time)
        if 0 <= timeInMin <= S:
            chatBeforeStartRecord[name].append(timeInMin)
        elif E <= timeInMin <= Q:
            chatEToQtRecord[name].append(timeInMin)
    except:
        break

answer = 0
for key in chatBeforeStartRecord.keys():
    if key in chatEToQtRecord:
        answer += 1
print(answer)