def solution(board, skill):
    # board
    N = len(board)
    M = len(board[0])
    accumulate_sum = [[0] * M for _ in range(N)]
    for s in skill:
        action, r1, c1, r2, c2, degree = s
        # 가로 누적 준비
        accumulate_sum[r1][c1] += (-1 * degree) if action == 1 else degree
        if c2 + 1 < M:
            accumulate_sum[r1][c2 + 1] += degree if action == 1 else (-1 * degree)
        # 세로 누적 준비
        if r2 + 1 < N:
            accumulate_sum[r2 + 1][c1] += degree if action == 1 else (-1 * degree)
            if c2 + 1 < M:
                accumulate_sum[r2 + 1][c2 + 1] += (-1 * degree) if action == 1 else degree
    
    # 가로 누적 계산
    for j in range(M):
        for i in range(N):
            accumulate_sum[i][j] += accumulate_sum[i][j - 1] if j - 1 >= 0 else 0
    # 세로 누적 계산
    for i in range(N):
        for j in range(M):
            accumulate_sum[i][j] += accumulate_sum[i - 1][j] if i - 1 >= 0 else 0
    
    # 결과 계산
    cnt = 0
    for i in range(N):
        for j in range(M):
            accumulate_sum[i][j] += board[i][j]
            if accumulate_sum[i][j] >= 1:
                cnt += 1
    return cnt