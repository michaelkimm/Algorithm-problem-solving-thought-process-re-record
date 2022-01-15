import sys
input = sys.stdin.readline

def GetSlicedRiceCake(ary, target):
  rt = 0
  for cake in ary:
    if cake - target >= 0:
      rt += (cake - target)
  return rt

# 입력
N, M = map(int, input().split())
riceCakeList = list(map(int, input().split()))

start = 0
end = max(riceCakeList)
result = 0

while start <= end:
  mid = (start + end) // 2
  total = GetSlicedRiceCake(riceCakeList, mid)
  # 떡의 양이 부족한 경우 더 많이 자르기 = 왼쪽 부터 탐색
  if total < M:
    end = mid - 1
  # 떡의 양이 많은 경우 더 적게 자르기 = 오른쪽 부터 탐색
  else:
    result = mid
    start = mid + 1

print(result)