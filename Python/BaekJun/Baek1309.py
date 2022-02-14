N = int(input())

left = 1
right = 1
empty = 1

for _ in range(1, N):
  preLeft = left
  preRight = right
  preEmpty = empty

  # 좌 = 이전 우 + 이전 빈 것
  left = preRight + preEmpty
  # 우 = 이전 좌 + 이전 빈 것
  right = preLeft + preEmpty
  # 빈 것 = 이전 좌 + 이전 우 + 이전 빈것
  empty = preLeft + preRight + preEmpty

result = sum([left, right, empty]) % 9901
print(result)