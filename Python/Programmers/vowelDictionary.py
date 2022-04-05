import itertools
def solution(word):
    words = []
    alphabets = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, len(alphabets) + 1):
        tmp_words = [''.join(chars) for chars in list(itertools.product(alphabets, repeat = i))]
        words += tmp_words
    words.sort()
    return words.index(word) + 1