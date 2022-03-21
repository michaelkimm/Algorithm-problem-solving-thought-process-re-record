def solution(N, road, K):
    answer = 0
    INF = int(1e10)
    dp = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][i] = 0
    for a, b, c in road:
        if dp[a][b] <= c:
            continue
        dp[a][b] = c
        dp[b][a] = c
    
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    
    for i in range(1, N + 1):
        if K >= dp[1][i]:
            answer += 1

    return answer