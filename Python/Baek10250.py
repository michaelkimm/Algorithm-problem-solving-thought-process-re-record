n = int(input())
dataList = []
clientRoomList = []

for _ in range(n):
  dataList.append(list(map(int, input().split())))

for data in dataList:
  H, W, N = data
  roomNum = ""
  # 층
  roomNum += str(H) if (N % H == 0) else str(N % H)

  # 호수
  # 꼭대기 층 아닐 경우, 꼭대기일 경우
  if N % H != 0:
    if (N / H + 1 < 10):
      roomNum += str(0)
    roomNum += str(int(N / H) + 1)
  else:
    if (N / H < 10):
      roomNum += str(0)
    roomNum += str(int(N / H))

  clientRoomList.append(roomNum)

for room in clientRoomList:
  print(room)