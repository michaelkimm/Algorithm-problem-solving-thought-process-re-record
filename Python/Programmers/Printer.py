from collections import deque

def solution(priorities, location):
  priorities_q = deque(priorities)
  target_location = location
  print_cnt = 0

  max_val = max(priorities_q)
  while priorities_q:
    l_value = priorities_q.popleft()
    if l_value != max_val:
      priorities_q.append(l_value)
    else:
      print_cnt += 1
      if target_location == 0:
        break
      max_val = max(priorities_q)


    target_location -= 1
    if target_location < 0:
      target_location = len(priorities_q) - 1

  answer = print_cnt
  return answer

  # ===================================================== #

  from collections import deque

def solution(priorities, location):
    priority_infos = deque([(priority, id) for id, priority in enumerate(priorities)])
    print_cnt = 0
    while priority_infos:
        popped_pri, popped_id = priority_infos.popleft()
        if any(popped_pri < pri for pri, id in priority_infos):
            priority_infos.append((popped_pri, popped_id))
        else:
            print_cnt += 1
            if popped_id == location:
                break
    
    answer = print_cnt
    return answer