import string
import math

tmp = string.digits+string.ascii_lowercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r] 
    else:
        return convert(q, base) + tmp[r]

def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임
    
def check_prime(stack):
    if not stack:
        return 0
    cnt = 0
    candi_num = int(''.join(stack))
    if is_prime_number(candi_num):
        cnt = 1
    return cnt

def solution(n, k):
    k_numeral_num = convert(n, k)
    stack = []
    cnt = 0
    for num in k_numeral_num:
        if num == '0':
            # stack 안의 숫자 문자 조합하여 소수인지 확인. 소수면 개수 += 1
            cnt += check_prime(stack)
            stack = []
            continue
        stack.append(num)
        
    cnt += check_prime(stack)
    stack = []
    
    return cnt