def solution(n):
    n_country = ['1', '2', '4']
    if n <= 3:
        return n_country[n - 1]
    
    s, r = divmod(n - 1, 3)
    return solution(s) + n_country[r]