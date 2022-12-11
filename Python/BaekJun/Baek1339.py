from collections import defaultdict
import sys
input = sys.stdin.readline


N = int(input())
weight = defaultdict(int)
words = []
for i in range(N):
    words.append(input().strip())
    for idx in range(len(words[i])):
        weight[words[i][idx]] += 10**(len(words[i]) - idx - 1)

dicts = dict()
weightList = sorted(weight.items(), key=lambda x:x[1], reverse=True)
value = 9
for ch, w in weightList:
    dicts[ch] = value
    value -= 1

sum = 0
for word in words:
    tmpNum = ''
    for ch in word:
        tmpNum += str(dicts[ch])
    sum += int(tmpNum)

print(sum)