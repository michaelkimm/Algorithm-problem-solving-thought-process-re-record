def solution(brown, yellow):
    # n은 0 ~ int(0.5 * brown) - 1
    # m은 0 ~ int(0.5 * brown) - 1
    answer = []
    for n in range(3, int(0.5 * brown) + 1):
        for m in range(3, int(0.5 * brown) + 1):
            if n + m == int(0.5 * brown) + 2 and (n - 2) * (m - 2) == yellow:
                answer = [n, m]
    return answer