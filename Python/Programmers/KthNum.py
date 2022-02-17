def solution(array, commands):
    answer = []
    
    for command in commands:
        s, e, i = command
        answer.append(sorted(array[s - 1:e])[i - 1])
    return answer