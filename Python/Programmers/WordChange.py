def diff_letter_cnt(a, b):
    return sum(x != y for x, y in zip(a, b))

def solution(begin, target, words):
    visited = [False] * len(words)
    
    cur_idx = 0
    stack = []
    for idx, word in enumerate(words):
            if not visited[idx] and diff_letter_cnt(begin, word) == 1:
                stack.append((word, idx, 1))
    
    change_cnt = 0
    word = ""
    while len(stack) > 0:
        word, cur_idx, change_cnt = stack.pop()
        visited[cur_idx] = True
        # change_cnt += 1
        if word == target:
            break
        
        for next_idx, next_word in enumerate(words):
            if not visited[next_idx] and diff_letter_cnt(word, next_word) == 1:
                stack.append((next_word, next_idx, change_cnt + 1))
    
    if word != target:
        change_cnt = 0
    
    return change_cnt