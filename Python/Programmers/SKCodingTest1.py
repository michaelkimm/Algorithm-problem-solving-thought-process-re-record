from itertools import permutations
def solution(goods):
    answer = []
    for good in goods:
        g_result = []
        for cnt in range(1, len(good) + 1):
            # cnt 길이의 연속적인 sub_string 구하기
            sub_strings = [good[i:i + cnt] for i in range(len(good) - cnt + 1)]
            for sub_str in sub_strings:
                key_avail = True
                if sub_str in g_result:
                    continue
                for g in goods:
                    if g == good:
                        continue
                    if sub_str in g:
                        key_avail = False
                        break
                if key_avail:
                    g_result.append(sub_str)
            if g_result:
                break
        # g_result 있는 경우
        if g_result:
            g_result.sort()
            g_result = ' '.join(g_result)
        # g_result 없는 경우
        else:
            g_result = "None"

        answer.append(g_result)

    return answer