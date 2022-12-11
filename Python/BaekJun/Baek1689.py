import sys
input = sys.stdin.readline

N = int(input())
pts = []
for _ in range(N):
    start, end = map(int, input().split())
    pts.append((start, 1))
    pts.append((end, -1))

pts.sort()

cnt = 0
answer = []
for pt, weight in pts:
    cnt += weight
    answer.append(cnt)

print(max(answer))