from itertools import product

def solution(rules, m):

    cases = list(product(range(len(rules)), repeat = m))

    answer = [0 for _ in range(len(rules))]
    for case in cases:
        startNum = case[0]
        curNum = startNum
        for i in range(1, len(case)):
            materialNum = case[i]
            curNum = rules[curNum][materialNum]

        answer[curNum] += 1

    for i in range(len(answer)):
        answer[i] = answer[i] % 10007
    return answer