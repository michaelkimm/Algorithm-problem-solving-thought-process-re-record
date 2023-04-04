import sys
input = sys.stdin.readline

N, K = map(int, input().split())
velocities = sorted(list(map(int, input().split())))

maxSum = 0
for pt in range(N - 1):
    leftSum = velocities[0] * (pt + 1)
    rightSum = velocities[pt + 1] * (N - (pt + 1))
    maxSum = max(leftSum + rightSum, maxSum)

div = K // maxSum
left = K % maxSum

if left == 0:
    print(div)
else:
    print(div + 1)
