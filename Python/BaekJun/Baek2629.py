import sys
input = sys.stdin.readline

N = int(input())
choos = [[]]
for v in sorted(list(map(int, input().split()))):
    choos.append([0] + [v])
ballCnt = int(input())
balls = list(map(int, input().split()))
maxBallWeight = 20

dp = [[0 for _ in range(maxBallWeight + 1)] for _ in range(N + 1)]
dp[0][0] = 1
for chooIdx in range(1, N + 1):
    for weight in range(maxBallWeight + 1):
        tmp = 0
        for choo in choos[chooIdx]:
            if weight - choo >= 0:
                tmp += dp[chooIdx - 1][weight - choo]
            # print(choo - weight)
            if maxBallWeight >= choo - weight >= 0 and (weight - choo) != (choo - weight):
                tmp += dp[chooIdx - 1][choo - weight]
        dp[chooIdx][weight] = tmp

for line in choos:
    print(line)

for line in dp:
    print(line)

answer = []
for ball in balls:
    if dp[N][ball] == 0:
        answer.append('N')
    else:
        answer.append('Y')

for a in answer:
    print(a, end = " ")
print()