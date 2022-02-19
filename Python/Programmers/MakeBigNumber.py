from collections import deque

def solution(number, k):
    num_q = deque([ch for ch in number])
    stack = [num_q.popleft()]
    # 증가되기 직전 값 제거, 끝까지 없다면 끝값 제거
    while num_q and k > 0:
        popped = num_q.popleft()
        while True:
            if len(stack) > 0 and stack[-1] < popped:
                stack.pop()
                k -= 1
                if k == 0:
                    stack.append(popped)
                    break
            else:
                stack.append(popped)
                break
    for _ in range(k):
        stack.pop()
    answer = ''.join(stack) + ''.join(list(num_q))
    return answer