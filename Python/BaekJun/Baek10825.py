import sys

N = int(sys.stdin.readline())
studentInfos = []
for _ in range(N):
  name, language, english, math = sys.stdin.readline().split()
  studentInfos.append((name, int(language), int(english), int(math)))

studentInfos.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for info in studentInfos:
  print(info[0])
