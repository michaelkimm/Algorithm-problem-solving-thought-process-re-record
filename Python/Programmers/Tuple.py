def solution(s):
    s = list(s[1:-1])
    set_list = []
    tmp_set = set()
    tmp_val = ""
    
    while s:
        pop_v = s.pop()
        if pop_v == '}':
            tmp_set = set()
        elif pop_v == ',':
            if s[-1] != '}':
                tmp_set.add(int(tmp_val[::-1]))
                tmp_val = "" 
        elif pop_v == '{':
            tmp_set.add(int(tmp_val[::-1]))
            set_list.append(tmp_set)
            tmp_val = ""
        else:
            tmp_val += pop_v
    
    set_list.sort(key=lambda x:len(x))
    result = [list(set_list[0])[0]]
    if len(set_list) == 1:
        return result
    for idx in range(len(set_list) - 1):
        diff_num = list(set_list[idx + 1].difference(set_list[idx]))[0]
        result.append(diff_num)
    
    return result


# ================================================ #

def solution(s):
    s = s.lstrip('{').rstrip('}').split('},{')
    s = sorted([v.split(',') for v in s], key = len)
    
    answer = []
    for v_list in s:
        for v in v_list:
            if v not in answer:
                answer.append(v)
                
    answer = [int(v) for v in answer]
    
    return answer