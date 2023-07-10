import math
import sys
input = sys.stdin.readline

N = int(input())
col_exists = [False for _ in range(N)]
right_up_diagonal = [False for _ in range(2 * N + 1)]
left_up_diagonal = [False for _ in range(2 * N + 1)]
answer = 0

def recursive(n, ci):
    global answer, N
    if n == N:
        answer += 1
        return
    
    for i in range(ci, N):
        for j in range(N):
            if col_exists[j] or right_up_diagonal[i + j] or left_up_diagonal[i - j + N]:
                continue
            col_exists[j] = True
            right_up_diagonal[i + j] = True
            left_up_diagonal[i - j + N] = True

            recursive(n + 1, i + 1)
            col_exists[j] = False
            right_up_diagonal[i + j] = False
            left_up_diagonal[i - j + N] = False

recursive(0, 0)
print(answer)
            