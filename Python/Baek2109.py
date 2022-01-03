import heapq

N = int(input())
lectureList = sorted([tuple(map(int, input().split())) for _ in range(N)], key = lambda x: (x[1], x[0]))

hp = []
maxDay = lectureList[len(lectureList) - 1][1] if len(lectureList) > 0 else 0
calendar = [0 for _ in range(maxDay + 1)]

for day in range(maxDay, 0, -1):
  # 비교할 렉쳐 모음이 없다면
  if len(lectureList) <= 0:
    if len(hp) > 0:
      calendar[day] = -heapq.heappop(hp)[0]
      continue
    else:
      break

  # 렉처 맨뒤 시간(가장 큰 시간)
  cmpAvailDay = lectureList[len(lectureList) - 1][1]
  # 현재 비교중인 시간이 오늘 날보다 크거나 같으면
  while cmpAvailDay >= day:
    heapq.heappush(hp, (-lectureList[len(lectureList) - 1][0], lectureList[len(lectureList) - 1][1]))
    lectureList.pop()
    if len(lectureList) > 0:
      cmpAvailDay = lectureList[len(lectureList) - 1][1]
    else:
      break

  if len(hp) > 0:
    calendar[day] = -heapq.heappop(hp)[0]

print(sum(calendar))


import sys
import heapq
input = sys.stdin.readline

N = int(input())
# pay, day
lectureList = sorted([tuple(map(int, input().split())) for _ in range(N)], key = lambda x: x[1])

hp = []

for pay, day in lectureList:
  heapq.heappush(hp, pay)
  if len(hp) > day:
    heapq.heappop(hp)

print(sum(hp))