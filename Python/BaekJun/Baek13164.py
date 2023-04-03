import sys
input = sys.stdin.readline

N, K = map(int, input().split())
heights = list(map(int, input().split()))

dh = []
for i in range(1, len(heights)):
  dh.append(heights[i] - heights[i - 1])

dh.sort(reverse=True)

print(sum(dh[K - 1:]))