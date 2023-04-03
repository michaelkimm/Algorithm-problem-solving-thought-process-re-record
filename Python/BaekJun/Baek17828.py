import sys
input = sys.stdin.readline

alphabetDict = dict()
for i in range(1, 27):
  alphabetDict[i] = chr(ord('A') + (i - 1))

N, X = map(int, input().split())

alphabets = ['A' for _ in range(N)]
if (N * 26) < X or N > X:
  print('!')
elif X >= N:
  X -= N
  for i in range(N - 1, -1, -1):
    if X > 25:
      X -= 25
      alphabets[i] = 'Z'
    elif X > 0:
      alphabets[i] = alphabetDict[X + 1]
      X = 0
      break
  print(''.join(alphabets))
