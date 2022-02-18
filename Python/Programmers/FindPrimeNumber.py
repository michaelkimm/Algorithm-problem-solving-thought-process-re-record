from itertools import permutations
from functools import reduce
import math

def check_prime_num(target):
    if target == 0 or target == 1:
      return False
  
    is_prime = True
    for num in range(2, int(math.sqrt(target)) + 1):
      if target % num == 0:
        is_prime = False
        break
    return is_prime

def str_sum(a, b):
    return a + b

def solution(numbers):
  answer = 0
  num_set = set()
  permu_list = []
  for cnt in range(1, len(numbers) + 1):
    # [('2', '3'), ('1', '2', '3')]
    permu_list += list(permutations(numbers, cnt))    

  for permu in permu_list:
    num_set.add(int(reduce(str_sum, permu)))

  for candi in num_set:
    if check_prime_num(candi):
      answer += 1

  return answer