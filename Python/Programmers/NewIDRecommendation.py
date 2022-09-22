def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2단계
    ret2 = ''
    for word in new_id:
        if word.isnumeric() or word.isalpha() or word in ['_', '-', '.']:
            ret2 += word
    # 3단계
    while '..' in ret2:
        ret2 = ret2.replace('..', '.')
    ret3 = ret2
    # 4단계
    ret4 = ret3.strip('.')
    # 5단계
    if ret4 == '':
        ret4 = 'a'
    ret5 = ret4
    # 6단계
    if len(ret5) >= 16:
        ret5 = ret5[:15].strip('.')
    ret6 = ret5
    # 7단계
    while len(ret6) <= 2:
        ret6 += ret6[-1]
    return ret6