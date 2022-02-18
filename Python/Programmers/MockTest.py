
def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0, 0, 0]
    for idx in range(len(answers)):
        if answers[idx] == p1[idx % len(p1)]:
            score[0] += 1
        if answers[idx] == p2[idx % len(p2)]:
            score[1] += 1
        if answers[idx] == p3[idx % len(p3)]:
            score[2] += 1

    result = []
    
    max_val = max(score)
    for idx, val in enumerate(score):
        if max_val == val:
            result.append(idx + 1)
        
    result.sort()
    
    return result