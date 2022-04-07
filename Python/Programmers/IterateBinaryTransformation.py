def solution(s):
    x = s
    transformed_cnt = 0
    zero_cnt = 0
    while x != '1':
        for w in x:
            if w == '0':
                zero_cnt += 1
        x = ''.join(['1' for w in x if w == '1'])
        x = bin(len(x))[2:]
        transformed_cnt += 1
    
    answer = [transformed_cnt, zero_cnt]
    return answer



# ====================================== #

def solution(s):
    x = s
    transformed_cnt = 0
    zero_cnt = 0
    while x != '1':
        one_cnt = x.count('1')
        zero_cnt += (len(x) - one_cnt)
        
        x = bin(one_cnt)[2:]
        transformed_cnt += 1
    
    answer = [transformed_cnt, zero_cnt]
    return answer