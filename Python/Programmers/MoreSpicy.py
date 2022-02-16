import heapq

def get_scoville(a, b):
    if a > b:
        return b + 2*a
    else:
        return a + 2*b

def solution(scoville, K):
    hp = sorted(scoville)
    heapq.heapify(hp)
    cnt = 0
    while hp and hp[0] < K:
        if len(hp) == 1:
            cnt = -1
            break
        cnt += 1
        s1 = heapq.heappop(hp)
        s2 = heapq.heappop(hp)
        tmp = get_scoville(s1, s2)
        heapq.heappush(hp, tmp)
    return cnt