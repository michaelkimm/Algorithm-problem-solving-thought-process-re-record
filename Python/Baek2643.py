N = int(input())
paperBox = sorted([sorted(map(int, input().split()), reverse = True) for _ in range(N)], reverse = True)

dp = [1 for _ in range(len(paperBox))]

for i in range(N):
  for j in range(i):
    # 현재 판단할 종이가 이전 계산된 부분 수열 최솟값보다 작은지
    if paperBox[i][1] <= paperBox[j][1]:
      dp[i] = max(dp[i], dp[j] + 1) 

print(max(dp))