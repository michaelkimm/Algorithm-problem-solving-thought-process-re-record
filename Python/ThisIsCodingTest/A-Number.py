import math
import time

N = int(input())

def GetBiggiestOne(target, lastNum):
  if target == 1:
    return 1
  elif target == lastNum:
    return lastNum

  dp = [lastNum]
  ten = 1

  while True:
    ten *= 10

    dpNum = dp[len(dp) - 1]

    for i in range(1, 10):
      # 비교할 수 구하기
      temp = dpNum + ten * i
      # 자리 수 구하기
      K = math.trunc(math.log10(temp) + 1)

      #print("temp:", temp, "K:", K)

      if temp > target - 1:
        print(dp)
        return dp[len(dp) - 1]
      if ((temp * temp) % (pow(10, K))) == temp:
        dp.append(temp)

start = time.time()

result = max(GetBiggiestOne(N, 5), GetBiggiestOne(N, 6))
print(result)

end = time.time()

print("time:", end - start)