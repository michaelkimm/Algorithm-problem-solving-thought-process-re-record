import sys

N = int(sys.stdin.readline())
houseList = list(map(int, sys.stdin.readline().split()))

houseList.sort()
middleIdx = len(houseList) // 2
if len(houseList) % 2 == 0:
  middleIdx -= 1  

print(houseList[middleIdx])