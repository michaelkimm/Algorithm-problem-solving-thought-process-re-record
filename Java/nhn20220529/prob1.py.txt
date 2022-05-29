def solution(cards1, cards2):
  n = len(cards1)
  answer = 0
  
  for i in range(n):
    card1set = set(cards1[i])
    card2set = set(cards2[i])
    if (len(card1set) != len(cards1[i])) or (len(card2set) != len(cards2[i])):
      answer += 1
      continue
    roundCardsSet = set(cards1[i] + cards2[i])
    if len(roundCardsSet) != (len(cards1[i]) + len(cards2[i])):
      answer += 1
      continue

    # 이전 카드 셋과 비교
    if (i != 0):
      if containsSameNumber(cards1[i], cards1[i - 1], 2) or containsSameNumber(cards2[i], cards2[i - 1], 2):
        answer += 1
        continue
    
  return answer

def containsSameNumber(ary1, ary2, targetCount):
  ary1set = set(ary1)
  ary2set = set(ary2)
  if len(ary1set.intersection(ary2set)) >= targetCount:
    return True
  else:
    return False