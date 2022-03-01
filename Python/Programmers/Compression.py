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