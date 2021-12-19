# 2차원 배열 회전 함수
def Turn2DArrayCW(ary):
  rowCnt = len(ary)
  colCnt = len(ary[0])
  result = []
  for colIdx in range(colCnt):
    newRow = []
    for rowIdx in range(rowCnt-1, -1, -1):
      newRow.append(ary[rowIdx][colIdx])
    result.append(newRow)
  return result
  
def Turn2DArrayCWs(ary, rotateCnt):
    result = ary
    for _ in range(rotateCnt):
      result = Turn2DArrayCW(result)
    return result