import sys
input = sys.stdin.readline

def CheckSettable(ary, minDist, wifiCnt):
  result = True
  # wifiCnt == 2 경우
  if wifiCnt == 2:
    if ary[len(ary) - 1] - ary[0] >= minDist:
      return True

  # wifiCnt > 2일 경우
  wifiLeft = wifiCnt - 2
  prePose = ary[0]
  for idx in range(1, len(ary) - 1):
    # 와이파이 다 쓴 경우
    if wifiLeft <= 0:
      break

    # 이전 wifi 위치와 minDist 보다 크거나 같으면
    if ary[idx] - prePose >= minDist:
      # 와이파이 배치
      prePose = ary[idx]  
      wifiLeft -= 1

  if wifiLeft > 0:
    result = False

  if ary[len(ary) - 1] - prePose < minDist:
    result = False

  return result


N, C = map(int, input().split())
houseList = []
for _ in range(N):
  houseList.append(int(input()))

houseList.sort()

start = 0
end = houseList[len(houseList) - 1]
result = 0

while start <= end:
  mid = (start + end) // 2

  isAvailable = CheckSettable(houseList, mid, C)

  # mid 최소 거리로 가능할 경우, 거리를 높여보자
  if isAvailable:
    result = max(result, mid)
    start = mid + 1
  # mid 최소 거리로 가능하지 않을 경우, 거리를 줄여보자
  else:
    end = mid - 1

print(result)
