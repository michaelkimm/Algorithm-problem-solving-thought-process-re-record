import sys

def get_factorial(n):
  if n == 0 or n == 1:
    return factorialResult[n]
    
  if factorialResult[n] == -1:
    factorialResult[n] = get_factorial(n - 1) * n
  return factorialResult[n]

def CalcCombi(n, k):
  return factorialResult[n] // factorialResult[k] // factorialResult[n - k]

input = sys.stdin.readline

N = int(input())
S = list(input().strip())

BigNum = int(1e10) + 7

# dp 사용
EAry = [0] * N
HAry = [0] * N

# 콤비네이션 계산 값 저장
factorialResult = [-1] * (N + 1)
factorialResult[0] = 1
factorialResult[1] = 1
for i in range(1, N + 1):
  get_factorial(i)

# E 배열 업데이트
ECount = 0
for i in range(N - 1, -1, -1):
  if S[i] == 'E':
    ECount += 1
  else:
    EAry[i] = EAry[i + 1] % BigNum if i + 1 < N else 0
    continue
  if ECount >= 2:
    for j in range(2, ECount + 1):
      EAry[i] += (CalcCombi(ECount, j) % BigNum)
      

# H 배열 업데이트
for i in range(N - 1, -1, -1):
  if S[i] != 'H':
    HAry[i] = HAry[i + 1] % BigNum if i + 1 < N else 0  
    continue
  # H일 경우
  if S[i] == 'H':
    if i + 1 < N and S[i + 1] == 'E':
      HAry[i] = (HAry[i + 1] + EAry[i + 1]) % BigNum
    elif i + 1 < N and S[i + 1] != 'E':
      HAry[i] = HAry[i + 1] % BigNum if i + 1 < N else 0
# print(EAry)
# print(HAry)

answer = 0
for i in range(N):
  if S[i] == 'W':
    answer += (HAry[i] % BigNum)

print(answer % BigNum)