import sys
input = sys.stdin.readline

n = int(input())
boxes = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for right in range(n):
    tmpMax = 0
    for left in range(right):
        if boxes[right] > boxes[left] and dp[left] + 1 > tmpMax:
            tmpMax = dp[left] + 1
            dp[right] = tmpMax

print(max(dp))
            
