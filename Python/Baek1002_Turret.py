n = int(input())

cntList = []

def GetP2Distance(x1_, y1_, x2_, y2_):
  return pow((x1_ - x2_), 2) + pow((y1_ - y2_), 2)

def CheckOverlap(x1_, y1_, r1_, x2_, y2_, r2_):
  if GetP2Distance(x1_, y1_, x2_, y2_) <= pow(r1_ - r2_, 2):
    return True
  else:
    return False

for _ in range(n):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  result = 0
  dist = GetP2Distance(x1, y1, x2, y2)
  # 한 원이 다른 원 안에 포함
  if (CheckOverlap(x1, y1, r1, x2, y2, r2)):
    # 한 원이 다른 원 안에 접하며 포함
    if dist == pow(r1 - r2, 2):
      # 원이 일치
      if r1 == r2:
        result = -1
      # 원 일치x
      else:
        result = 1
    # 한 원이 다른 원 안에 접하지 않으면서 포함
    else:
      result = 0
  # 한 원이 다른 원에 포함x
  else:
    # 두 점 사이 거리가 두 반지름 합보다 작을 경우
    if (dist < pow(r1 + r2, 2)):
      result = 2
    # 클 경우
    elif (dist > pow(r1 + r2, 2)):
      result = 0
    # 같을 경우
    else:
      result = 1

  cntList.append(result)

for i in range(len(cntList)):
  print(cntList[i])