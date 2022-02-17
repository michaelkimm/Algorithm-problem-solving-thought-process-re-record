from functools import cmp_to_key

def my_cmp(x, y):
  result = 0
  if x + y > y + x:
    result = 1
  elif x + y < y + x:
    result = -1
  else:
    result = 0
  return result

def solution(numbers):
  # 앞자리수가 높은 순서, 자리수가 적은게 높은 순서 
  numbers = [str(num) for num in numbers]
  str_numbers = sorted(numbers, reverse = True, key=cmp_to_key(my_cmp))

  result = ''
  front_zero_erase = False
  for num in str_numbers:
    if num == 0 and not front_zero_erase:
      continue
    result += str(num)
    front_zero_erase = True
  return str(int(result))