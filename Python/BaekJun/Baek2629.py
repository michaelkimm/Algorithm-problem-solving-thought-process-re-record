from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
choos = [[]]
for v in sorted(list(map(int, input().split()))):
    choos.append([0] + [v])
ballCnt = int(input())
balls = list(map(int, input().split()))
ballSum = sum(sum(cs) for cs in choos)

dp = [defaultdict(int) for _ in range(N + 1)]
dp[0][0] = 1
for chooIdx in range(1, N + 1):
    for weight in range(-ballSum, ballSum + 1):
        tmp = 0
        for choo in choos[chooIdx]:
            # 추를 공 반대 편에 두는 경우
            tmp += dp[chooIdx - 1][weight - choo]
            # 추를 공과 같이 두는 경우
            tmp += dp[chooIdx - 1][weight + choo]
        dp[chooIdx][weight] = tmp

answer = []
for ball in balls:
    if dp[N][ball] == 0:
        answer.append('N')
    else:
        answer.append('Y')

for a in answer:
    print(a, end = " ")
print()