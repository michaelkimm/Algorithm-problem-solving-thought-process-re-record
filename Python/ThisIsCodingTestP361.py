def solution(N, stages):
    answer = []
    # 계수 정렬
    countSortedList = [0] * (N + 2)
    for stage in stages:
        countSortedList[stage] += 1
    
    # 실패율 = k 갯수 / k 스테이지 보다 크거나 같은 숫자의 갯수
    total = sum(countSortedList)
    for i in range(1, len(countSortedList) - 1):
        if total == 0:
            answer.append((i, 0))
        else:
            answer.append((i, countSortedList[i] / total))
        total -= countSortedList[i]
    
    answer.sort(key = lambda x: (float(-x[1]), float(x[0])))
    answer = [i[0] for i in answer]
    return answer