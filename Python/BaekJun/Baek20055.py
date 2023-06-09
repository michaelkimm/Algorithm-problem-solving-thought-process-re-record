from collections import deque
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
durabilitys = deque(list(map(int, input().split())))
haveRobots = deque([False for _ in range(2 * N)])


zeroCnt = 0
result = 1
while (zeroCnt < K):
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    durabilitys.rotate(1)
    haveRobots.rotate(1)
    haveRobots[N - 1] = False

    # 로봇 이동
    if any(haveRobots):
        for robotIdx in range(N - 2, -1, -1):
            # 현재 칸에 로봇 있고, 다음 칸에 로봇 없고, 다음 칸에 내구도가 1 이상 남아 있어야함.
            if haveRobots[robotIdx] and not haveRobots[robotIdx + 1] and durabilitys[robotIdx + 1] >= 1:
                haveRobots[robotIdx + 1] = True
                haveRobots[robotIdx] = False
                durabilitys[robotIdx + 1] -= 1
                if durabilitys[robotIdx + 1] == 0:
                    zeroCnt += 1
                if robotIdx + 1 == N - 1:
                    haveRobots[N - 1] = False

    # 올리는 위치에 로봇 올리기
    if durabilitys[0] > 0:
        haveRobots[0] = True
        durabilitys[0] -= 1
        if durabilitys[0] == 0:
            zeroCnt += 1
    result += 1

print(result - 1)