from collections import defaultdict
import sys
input = sys.stdin.readline

class AlphabetInfo:
    def __init__(self, alphabet, highestDigit):
        self.alphabet = alphabet
        self.highestDigit = highestDigit
        self.count = 1

    def __str__(self):
        return "alphabet:" + str(self.alphabet) + "\thighestDigit:" + str(self.highestDigit) + "\tcount:" + str(self.count)

    def checkHighestDigit(self, newDigit):
        if self.highestDigit < newDigit:
            self.highestDigit = newDigit

    def increaseCount(self):
        self.count += 1

N = int(input())
words = []
for i in range(N):
    words.append(input().strip())
    words[i] = words[i][::-1]

alphabetInfoDict = dict()

for i in range(N):
    for idx, ch in enumerate(words[i]):
        if ch in alphabetInfoDict.keys():
            alphabetInfoDict[ch].checkHighestDigit(idx)
            alphabetInfoDict[ch].increaseCount()
        else:
            alphabetInfoDict[ch] = AlphabetInfo(ch, idx)

alphabetInfoList = []
for key, item in alphabetInfoDict.items():
    alphabetInfoList.append(item)

alphabetInfoList.sort(key=lambda x:(x.highestDigit, x.count), reverse=True)

for info in alphabetInfoList:
    print(info)

alphabetWeightDict = defaultdict(int)
for idx, alphabetInfo in enumerate(alphabetInfoList):
    ch = alphabetInfo.alphabet
    alphabetWeightDict[ch] += (9 - idx)


for idx in range(len(words)):
    for key in alphabetWeightDict.keys():
        words[idx] = words[idx].replace(key, str(alphabetWeightDict[key]))
    words[idx] = words[idx][::-1]

print(words)
sum = sum([int(val) for val in words])
print(sum)