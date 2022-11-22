import sys
input = sys.stdin.readline

def flip(word, i):
    return word[:i + 1][::-1] + word[i+1:]

S = input().strip()

for i in range(1, len(S)):
    if i == len(S) - 1:
        if S[0] > S[i]:
            # 뒤집기
            S = flip(S, i)
        break

    if S[0] > S[i]:
        if S[i] < S[i + 1]:
            # 뒤집기
            S = flip(S, i)
    else:
        if S[i] > S[i + 1] and S[0] >= S[i + 1]:
            # 뒤집기
            S = flip(S, i)

print(S)
