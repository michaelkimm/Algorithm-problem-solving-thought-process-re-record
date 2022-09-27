import sys
input = sys.stdin.readline

def getMaxEared(buyCheckList, prices, N):
    earned = 0
    basket = []
    for idx in range(N):
        if buyCheckList[idx] >= 1:
            # 구매
            basket.append(prices[idx])
        elif buyCheckList[idx] == 0:
            for price in basket:
                earned += (prices[idx] - price)
            basket = []
    return earned    

def getBuyCheckList(prices, N):
    dp = [0 for _ in range(N)]
    tmpMaxVal = prices[N - 1]
    for idx in range(N - 2, -1, -1):
        dp[idx] = dp[idx + 1] + 1 if prices[idx] <= tmpMaxVal else 0
        tmpMaxVal = max(tmpMaxVal, prices[idx])
    return dp

T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    # 미리 계산
    dp = getBuyCheckList(prices, N)
    
    # 구매할 것 택하기
    earned = getMaxEared(dp, prices, N)
    
    answer.append(earned)

for line in answer:
    print(line)