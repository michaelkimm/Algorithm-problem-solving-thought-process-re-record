def solution(money):
    # 첫째 집을 뽑은 경우
    # 첫번째 = 나를 안뽑은 경우, 두번째 = 나를 뽑은 경우
    dp = [[0, 0] for _ in range(len(money))]
    for i in range(len(money)):
        if i == 0:
            dp[i] = [0, money[i]]
        elif i == 1:
            dp[i] = [money[0], money[0]]
        elif i == len(money) - 1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = [max(dp[i - 1][0], dp[i - 1][1]), dp[i - 1][0] + money[i]]
    
    first_picked = max(dp[-1])
    
    # 첫째 집을 안뽑은 경우
    # 첫번째 = 나를 안뽑은 경우, 두번쨰 = 나를 뽑은 경우
    dp = [[0, 0] for _ in range(len(money))]
    for i in range(len(money)):
        if i == 0:
            dp[i] = [0, 0]
        else:
            dp[i] = [max(dp[i - 1][0], dp[i - 1][1]), dp[i - 1][0] + money[i]]
    
    first_not_picked = max(dp[-1])
    
    answer = max(first_picked, first_not_picked)
    return answer


# =============================================================== #
def solution(money):
    # 첫째 집을 뽑은 경우
    # 첫번째 = 나를 안뽑은 경우, 두번째 = 나를 뽑은 경우
    dp1 = [[0, 0] for _ in range(len(money))]
    dp1[0] = [money[0], money[0]]
    dp1[1] = [money[0], money[0]]
    
    # 첫째 집을 안뽑은 경우
    # 첫번째 = 나를 안뽑은 경우, 두번쨰 = 나를 뽑은 경우
    dp2 = [[0, 0] for _ in range(len(money))]
    dp2[1] = [0, money[1]]
    
    for i in range(2, len(money)):
        dp1[i] = [max(dp1[i - 1][0], dp1[i - 1][1]), dp1[i - 1][0] + money[i]]
        dp2[i] = [max(dp2[i - 1][0], dp2[i - 1][1]), dp2[i - 1][0] + money[i]]
    
    dp1[len(money) - 1] = dp1[len(money) - 2]
    
    answer = max(max(dp1[-1]), max(dp2[-1]))
    return answer