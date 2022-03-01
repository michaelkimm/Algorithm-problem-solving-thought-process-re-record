def check_correct_string(w):
  stack = []
  for bracket in w:
    if not stack:
      stack.append(bracket)
    elif stack[-1] == '(' and bracket == ')':
      stack.pop()
    else:
      stack.append(bracket)

  if stack:
    return False
  else:
    return True

def get_balanced_string(w):
  string = ""
  left, right = 0, 0
  for bracket in w:
    if bracket == '(':
      left += 1
    else:
      right += 1
    string += bracket
    if left == right:
      break
  return string, w[len(string):]

def solution(p):
  if p == "":
    return ""
  u, v = get_balanced_string(p)
  if check_correct_string(u):
    v_result = solution(v)
    return u + v_result
  else:
    ary = "(" + solution(v) + ")"
    u_result = "".join(')' if ch == '(' else '(' for ch in u[1:-1]) 
    return ary + u_result