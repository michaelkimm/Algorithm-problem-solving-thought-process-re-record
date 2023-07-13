import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))
picked = [False for _ in range(N)]
answerSet = set()
answer = 0

def usable(stack):
    global N, L, R, X
    if not (L <= sum(stack) <= R):
        return False
    if abs(min(stack) - max(stack)) < X:
        return False
    return True
    
def recursive(curIdx, stack, step):
    global N, L, R, X, problems, answer, answerSet, picked
    if curIdx >= N:
        if len(stack) >= 2 and usable(stack):
            answerSet.add(''.join([str(v) for v in stack]))
            answer += 1
        return

    # 뽑는 경우
    stack.append(problems[curIdx])
    recursive(curIdx + 1, stack, step + 1)
    stack.pop()

    # 안뽑는 경우
    recursive(curIdx + 1, stack, step + 1)

recursive(0, [], 0)
print(answer)