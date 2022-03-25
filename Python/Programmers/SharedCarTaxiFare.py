def solution(n, s, a, b, fares):
    INF = int(1e10)
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 0
    for u, v, c in fares:
        dp[u][v] = c
        dp[v][u] = c
    
    for m in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][m] + dp[m][j])
                
    distances = [0] * (n + 1)
    for i in range(1, n + 1):
        distances[i] = dp[s][i] + dp[i][a] + dp[i][b]
        
    answer = min(distances[1:])
    return answer