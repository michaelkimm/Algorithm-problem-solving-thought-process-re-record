def solution(citations):
    sorted_citations = sorted(citations, reverse=True)
    h = 0
    for idx in range(len(sorted_citations)):
        if sorted_citations[idx] >= idx + 1:
            h = idx + 1
        else:
            break
    answer = h
    return answer