import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0] * (N + 1)

for idx, num in enumerate(nums):
    dp[idx + 1] = num
    dp[idx + 1] += dp[idx]

left = 0
right = 1
minLen = int(1e6)
while left < len(dp) and right < len(dp):
    tempSum = dp[right] - dp[left]
    sumLen = right - left
    if tempSum >= S:
        if sumLen < minLen:
            minLen = sumLen
        left += 1
    elif tempSum < S:
        right += 1

if left == 0 and right == len(dp):
    minLen = 0
print(minLen)
