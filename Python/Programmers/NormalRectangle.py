import math

def get_unusable_cnt(w, h):
    if w == 1:
        return h
    elif h == 1:
        return w
    gcd_num = math.gcd(w, h)
    print("gcd_num:", gcd_num)
    unusable_cnt = 0
    if gcd_num != 1:
        unusable_cnt = gcd_num * get_unusable_cnt(w // gcd_num, h // gcd_num)
    else:
        unusable_cnt =  w + h - 1
    print(unusable_cnt)
    return unusable_cnt

def solution(w,h):
    
    return w * h - get_unusable_cnt(w, h)

# ================================================= #
import math

def solution(w,h):
    gcd_v = math.gcd(w, h)
    return w * h - gcd_v * (w // gcd_v + h // gcd_v - 1)