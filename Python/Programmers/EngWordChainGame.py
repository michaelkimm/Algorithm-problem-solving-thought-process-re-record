def solution(n, words):
    word_set = set()
    cycle = 1
    number = 1
    is_perfect = True
    before_word = words[0][0]
    for word in words:
        if word in word_set or before_word[-1] != word[0] :
            is_perfect = False
            break
        word_set.add(word)
        number += 1
        if number > n:
            number = 1
            cycle += 1
            
        before_word = word
    if is_perfect:
        number = 0
        cycle = 0

    answer = [number, cycle]
    return answer