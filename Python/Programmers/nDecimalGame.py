import string

tmp = string.digits+string.ascii_uppercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    '''
    최대 m * t 숫자가 n진법으로 바뀌어야함.
    '''
    all_num = ""
    for num in range(m * t):
        all_num += convert(num, n)

    answer = ""
    for idx, candidate_num in enumerate(all_num):
        if (idx % m + 1) == p:
            t -= 1
            answer += candidate_num        
            if t == 0:
                break
    
    return answer