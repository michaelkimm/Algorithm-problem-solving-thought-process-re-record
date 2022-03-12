def solution(n, clockwise):
  answer = [[0] * n for _ in range(n)]
  spin_needed = n // 2 + n % 2
  cur_spin_cnt = 1
  start_num, end_num = 1, n - 1
  direction = 0
  if clockwise:
    for _ in range(spin_needed):
      # 위
      direction = 0
      for _ in range(4):
        if direction == 0:
          for j in range(end_num - start_num + 1):
            answer[cur_spin_cnt - 1][cur_spin_cnt - 1 + j] = start_num + j
        elif direction == 1:
          for i in range(end_num - start_num + 1):
            answer[cur_spin_cnt - 1 + i][n - cur_spin_cnt] = start_num + i
        elif direction == 2:
          for j in range(end_num - start_num + 1):
            answer[n - cur_spin_cnt][n - cur_spin_cnt - j] = start_num + j
        elif direction == 3:
          for i in range(end_num - start_num + 1):
            answer[n - cur_spin_cnt - i][cur_spin_cnt - 1] = start_num + i
        direction += 1
        if direction == 4:
            direction = 0
      cur_spin_cnt += 1
      start_num = end_num + 1
      if (n - 2 * (cur_spin_cnt - 1)) >= 2:
        end_num = start_num + (n - 2 * (cur_spin_cnt - 1)) - 2
      else:
        end_num = start_num
  else:
    for _ in range(spin_needed):
      # 위
      direction = 0
      for _ in range(4):
        if direction == 0:
          for i in range(end_num - start_num + 1):
            #answer[cur_spin_cnt - 1 + i][n - cur_spin_cnt] = start_num + i
            answer[cur_spin_cnt - 1 + i][cur_spin_cnt - 1] = start_num + i
        elif direction == 1:
          for j in range(end_num - start_num + 1):
            answer[n - cur_spin_cnt][cur_spin_cnt - 1 + j] = start_num + j
        elif direction == 2:
          for i in range(end_num - start_num + 1):
            #answer[n - cur_spin_cnt - i][cur_spin_cnt - 1] = start_num + i
            answer[n - cur_spin_cnt - i][n - cur_spin_cnt] = start_num + i
        elif direction == 3:
          for j in range(end_num - start_num + 1):
            answer[cur_spin_cnt - 1][n - cur_spin_cnt - j] = start_num + j
        direction += 1
        if direction == 4:
            direction = 0
      cur_spin_cnt += 1
      start_num = end_num + 1
      if (n - 2 * (cur_spin_cnt - 1)) >= 2:
        end_num = start_num + (n - 2 * (cur_spin_cnt - 1)) - 2
      else:
        end_num = start_num

  return answer
result = solution(1, True)
for line in result:
  print(line)

import math
print(math.factorial(0))