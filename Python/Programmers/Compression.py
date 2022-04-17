from collections import OrderedDict

def solution(msg):
  # 단어 사전 초기화
  word_dict = OrderedDict()
  last_num = 0
  for i in range(0, 26):
    word_dict[chr(65 + i)] = i + 1
    last_num = i + 1
      
  compressed = []    
  
  left = 0
  while left <= len(msg) - 1:
    if left == len(msg) - 1:
      compressed.append(word_dict[msg[-1]])
      break
    for right in range(len(msg) - 1, left - 1, -1):
      if msg[left:right + 1] in word_dict:
        compressed.append(word_dict[msg[left:right + 1]])
        word_dict[msg[left:right + 2]] = last_num + 1
        last_num += 1
        left = right + 1
        break
      
  answer = compressed
  return answer


  # ====================================================  #

  def solution(msg):
    word_dict = { chr(64 + idx) for idx in range(1, 27)}
    
    answer = []
    left, right = 0, 0
    while left < len(msg):
        right = left
        while right < len(msg) and msg[left:right + 1] in word_dict:
            right += 1
        if right < len(msg):
            word_dict[msg[left:right + 1]] = len(word_dict) + 1
        answer.append(word_dict[msg[left:right]])
        left = right
    
    return answer



  # ============================================== #

  def solution(msg):
    word_dict = {chr(64 + idx):idx for idx in range(1, 27)}
    
    answer = []
    while msg:
        right = 0
        w = ''
        while right < len(msg) and msg[:right + 1] in word_dict:
            right += 1
        right -= 1
        w = msg[:right + 1]
        
        answer.append(word_dict[w])
        msg = msg[right + 1:]
        if msg:
            word_dict[w + msg[0]] = len(word_dict) + 1
    
    return answer