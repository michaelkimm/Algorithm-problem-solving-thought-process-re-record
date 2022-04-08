def solution(n, left, right):
    left = int(left)
    right = int(right)
    si = left // n
    sj = left % n
    ei = right // n
    ej = right % n
    answer = []
    for i in range(si, ei + 1):
        for j in range(n):
            if left <= i * n + j <= right:
                val = i + 1 if i >= j else j + 1
                answer.append(val)
    return answer