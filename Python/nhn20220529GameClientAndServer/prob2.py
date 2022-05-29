def solution(balance, transaction, abnormal):
  # abnormal은 오름차순, 1 <= abnormal < n
  userBuckets = [[(v, idx + 1)] for idx, v in enumerate(balance)]
  userBuckets.insert(0, [(0, 0)])

  for t in transaction:
    fromUser, toUser, value = t

    # print("유저", fromUser, "에게서", value, "인출 후", toUser, "에게 입금")
    # print("인출 전", fromUser, "버킷: ", userBuckets[fromUser])
    # print("인출 전", toUser, "버킷: ", userBuckets[toUser])
    
    withdrawLog = withdraw(userBuckets[fromUser], value)
    deposit(userBuckets[toUser], withdrawLog)
    
    # print("인출한 로그: ", withdrawLog)
    
    # print("인출한 후", fromUser, "버킷: ", userBuckets[fromUser])
    # print("입금 후", toUser, "버킷: ", userBuckets[toUser])
    # print("")

  answer = [0 for _ in range(len(balance))]

  for id, logBucket in enumerate(userBuckets):
    if id == 0:
      continue
    # print(logBucket)
    for log in logBucket:
      if not log[1] in abnormal:
        answer[id - 1] += log[0]
  
  return answer

def withdraw(fromUserBucket, value):
  returnBucket = []
  totalValue = 0
  # value 이상 만큼 뽑기.
  while totalValue < value:
    tradeLog = fromUserBucket.pop()
    returnBucket.append(tradeLog)
    # 40
    totalValue += tradeLog[0]
    
  # value에 딱 맞게 쪼개서 다시 넣기
  if (totalValue > value):
    # 마지막으로 뽑기한 로그 pop == 30
    log = returnBucket.pop()
    # (10 + 30) - 20 = 20
    # 더 뽑은 양
    dv = totalValue - value
    
    needToBeInBucketLog = (dv, log[1])
    needToBeExtractedLog = (log[0] - dv, log[1])
    
    fromUserBucket.append(needToBeInBucketLog)
    returnBucket.append(needToBeExtractedLog)
  return returnBucket

def deposit(toUserBucket, withdrawLog):
  toUserBucket += withdrawLog
  
b = [100, 1, 1, 1, 1]
t = [[1, 2, 100], [2, 3, 101], [3, 4, 102], [4, 5, 103], [5, 1, 104]]
a = [1]

print(solution(b, t, a))