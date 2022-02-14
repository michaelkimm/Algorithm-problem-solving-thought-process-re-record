import sys
input = sys.stdin.readline

N, x = map(int, input().split())
numAry = list(map(int, input().split()))

def bisect_dir(ary, target, searchLeftBoundary):
  start = 0
  end = len(ary) - 1
  result = -1
  
  while start <= end:
    mid = (start + end) // 2
    if ary[mid] == target:
      # left 경우
      if (searchLeftBoundary):
        if mid - 1 < 0 or ary[mid - 1] != target:
          result = mid
          break
        else:
          end = mid - 1
      # right 경우
      else:
        if mid + 1 > len(ary) - 1 or ary[mid + 1] != target:
          result = mid
          break
        else:
          start = mid + 1  
    elif ary[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return result

rightIdx = bisect_dir(numAry, x, False)
leftIdx = bisect_dir(numAry, x, True)

if (rightIdx == -1 or leftIdx == -1):
  cnt = -1
else:
  cnt = rightIdx - leftIdx + 1
print(cnt)