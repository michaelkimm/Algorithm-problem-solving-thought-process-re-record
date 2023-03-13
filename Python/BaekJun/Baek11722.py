import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp = [0 for _ in range(N)]

for i in range(len(numbers)):
    for j in range(i + 1):
        if numbers[j] == numbers[i]:
            dp[i] = dp[j] if dp[j] != 0 else 1
        elif numbers[j] > numbers[i]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

print(dp)

print(max(dp))