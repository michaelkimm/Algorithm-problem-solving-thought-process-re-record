import sys
input = sys.stdin.readline

N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))

if N == 1:
    print(stairs[1])
    exit()
elif N == 2:
    print(sum(stairs))
    exit()

dp = [[0 for _ in range(3)] for _ in range(N + 1)]
# i = 계단 인덱스, j = 연속 오른 횟수 
dp[1][1] = stairs[1]
dp[2][1] = stairs[2]
dp[2][2] = stairs[1] + stairs[2]
for i in range(3, N + 1):
    dp[i][2] = stairs[i] + dp[i - 1][1]
    dp[i][1] = stairs[i] + max(dp[i - 2][1], dp[i - 2][2])
print(max(dp[-1][1:]))