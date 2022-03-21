def solution(n):
    answer = 0
    bf = 1
    bbf = 0
    cur = 1
    for _ in range(n):
        cur = bf + bbf
        bbf, bf = bf, cur
    return cur % 1000000007