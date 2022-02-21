di = [0, 1]
dj = [1, 0]

def solution(m, n, puddles):
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for x, y in puddles:
        dp[y][x] = -1
        
    dp[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:
              continue
            for k in range(2):
                ni = i + di[k]
                nj = j + dj[k]
                if ni > n or nj > m:
                    continue
                if dp[ni][nj] != -1:
                    dp[ni][nj] += dp[i][j]
    
    answer = dp[n][m] % 1000000007
    return answer