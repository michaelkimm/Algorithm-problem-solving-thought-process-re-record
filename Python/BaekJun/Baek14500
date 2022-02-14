N, M = map(int, input().split())
paper = []

for _ in range(N):
  paper.append(list(map(int, input().split())))

tets = [
  [[1, 1, 1, 1]],           # ====
  [[1], [1], [1], [1]],
  [[1, 1], [1, 1]],         # 네모
  [[1, 0], [1, 0], [1, 1]], # ㄴ
  [[1, 1, 1], [1, 0, 0]],
  [[1, 1], [0, 1], [0, 1]],
  [[0, 0, 1], [1, 1, 1]],
  [[0, 1], [0, 1], [1, 1]], # ㄴ 대칭
  [[1, 0, 0], [1, 1, 1]],
  [[1, 1], [1, 0], [1, 0]],
  [[1, 1, 1], [0, 0, 1]],
  [[1, 1, 1], [0, 1, 0]],   # ㅗ
  [[0, 1], [1, 1], [0, 1]],
  [[0, 1, 0], [1, 1, 1]],
  [[1, 0], [1, 1], [1, 0]],
  [[1, 0], [1, 1], [0, 1]], # ㄹ
  [[0, 1, 1], [1, 1, 0]],
  [[0, 1], [1, 1], [1, 0]], # ㄹ 대칭
  [[1, 1, 0], [0, 1, 1]]
]


def CheckKernelInArray(kernel_, array_, si, sj):
  tetRowSize = len(kernel_)
  tetColSize = len(kernel_[0])
  if si + tetRowSize - 1 > len(array_) - 1 or sj + tetColSize - 1 > len(array_[0]) - 1:
    return False
  return True

def CalculateConv(kernel_, ary_, si, sj):
  result = 0
  for i in range(len(kernel_)):
    for j in range(len(kernel_[0])):
      result += kernel_[i][j] * ary_[si + i][sj + j]
  return result

maxVal = 0

# 각 테트로미노
for tet in tets:
  # 순회
    for i in range(len(paper)):
      for j in range(len(paper[0])):
        # 테트로미노 처음과 끝이 종이 안에 없으면
        if (CheckKernelInArray(tet, paper, i, j) != True):
          continue

        # Convolution 계산
        calVal = CalculateConv(tet, paper, i, j)
        # 최대 값이면 업데이트
        maxVal = max(maxVal, calVal)
    

print(maxVal)