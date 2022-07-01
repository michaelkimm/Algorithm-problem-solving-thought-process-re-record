from collections import defaultdict
import sys
input = sys.stdin.readline

def getCumulativeSum(ary):
  culmulativeSum = [0 for i in range(len(ary) + 1)]
  for i in range(1, len(ary) + 1):
    culmulativeSum[i] = culmulativeSum[i - 1] + ary[i - 1]
  return culmulativeSum

def getSumCases(ary):
  sums = []
  for i in range(len(ary)):
    for j in range(i + 1, len(ary)):
      sums.append(ary[j] - ary[i])
  sums.sort()
  return sums

def getNumCntDict(ary):
  cntDict = defaultdict(int)
  for v in ary:
    cntDict[v] += 1
  return cntDict

def getCompressedSortedList(ary):
  return sorted(list(set(ary)))
  
# input
T = int(input())
n = int(input())
AInput = input().split()
A = [int(v) for v in AInput]
m = int(input())
BInput = input().split()
B = [int(v) for v in BInput]

ACulmulativeSum = getCumulativeSum(A)
BCulmulativeSum = getCumulativeSum(B)
AarraySums = getSumCases(ACulmulativeSum)
BarraySums = getSumCases(BCulmulativeSum)

ASumCntDict = getNumCntDict(AarraySums)
BSumCntDict = getNumCntDict(BarraySums)

ASumCompresseds = getCompressedSortedList(AarraySums)
BSumCompresseds = getCompressedSortedList(BarraySums)

left = 0
right = len(BSumCompresseds) - 1

answer = 0
# 조건 주의!
while left < len(ASumCompresseds) and right >= 0:
  result = ASumCompresseds[left] + BSumCompresseds[right]
  if result == T:
    answer += (ASumCntDict[ASumCompresseds[left]] * BSumCntDict[BSumCompresseds[right]])
    right -= 1
  elif result > T:
    right -= 1
  elif result < T:
    left += 1

print(answer)