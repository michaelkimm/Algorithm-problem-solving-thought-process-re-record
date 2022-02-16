def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack and stack[-1][0] > prices[i]:
            top_v, top_idx = stack.pop()
            answer[top_idx] = i - top_idx
        stack.append((prices[i], i))
        
    while stack:
        top_v, top_idx = stack.pop()
        answer[top_idx] = len(prices) - 1 - top_idx
    return answer