import sys
input = sys.stdin.readline

N, M = map(int, input().split())
strSet = set([input().strip() for _ in range(N)])
checkList = [input().strip() for _ in range(M)]
answer = 0

for string in checkList:
    if string in strSet:
        answer += 1

print(answer)
