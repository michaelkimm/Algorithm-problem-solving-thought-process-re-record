import sys
input = sys.stdin.readline

words = list(input().strip())
for i in range(len(words)):
    if words[i:] == words[i:][::-1]:
        print(i + len(words))
        break