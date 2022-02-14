import heapq
import sys
input = sys.stdin.readline

N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]

# 시작 시간 순으로 정렬
schedules.sort()
# 진행중인 회의 저장
hp = []
# 최대 회의 갯수
maxRoomCnt = 0

# 회의 순회
for start, end in schedules:
  # 최소 힙 젤 빨리 끝나는 회의 지금 시간대 지났으면 꺼내기 until 안끝나는 회의 있을 때 까지
  while len(hp) > 0 and hp[0] <= start:
    heapq.heappop(hp)
  # 진행중인 회의 저장 = 끝나는 시간으로 최소 힙 푸시
  heapq.heappush(hp, end)
  # 최대 회의 갯수 업데이트
  maxRoomCnt = max(maxRoomCnt, len(hp))

print(maxRoomCnt)
