import sys
input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))

def bisect_fixedPoint(targetAry):
  start = 0
  end = len(targetAry) - 1
  result = -1

  while start <= end:
    mid = (start + end) // 2
    if targetAry[mid] == mid:
      result = mid
      break
    elif targetAry[mid] < mid:
      start = mid + 1
    else:
      end = mid - 1

  return result

print(bisect_fixedPoint(ary))