import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = sorted(list(map(int, input().split())))

minusList = []
plusList = []
distList = []
maxDist = 0

# 플러스 마이너스 나누기. 최대 거리 값 찾기
for book in books:
  if book > 0:
    plusList.append(book)
  else:
    minusList.append(book)
  
  if abs(book) > abs(maxDist):
    maxDist = book

plusList.sort(reverse = True)

# 플러스 값 처리
for i in range(0, len(plusList), M):
  if plusList[i] != maxDist:
    distList.append(plusList[i])
# 마이너스 값 처리
for i in range(0, len(minusList), M):
  if minusList[i] != maxDist:
    distList.append(minusList[i])

# 최대 값 처리
result = abs(maxDist)
# 남은 값 처리
for dist in distList:
  result += abs(dist * 2)

print(result)