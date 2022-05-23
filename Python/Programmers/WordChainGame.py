def solution(n, words):
    answer = []
    prev_word = words[0]
    showed_words = set([prev_word])
    dropout_exist = False
    
    for i in range(1, len(words)):
        turn = i % n + 1
        if words[i] in showed_words or words[i][0] != prev_word[-1]:
            cycle = i // n + 1
            answer = [turn, cycle]
            dropout_exist = True
            break
        prev_word = words[i]
        showed_words.add(words[i])
    
    if not dropout_exist:
        answer = [0, 0]
    return answer