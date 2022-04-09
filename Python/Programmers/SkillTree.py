from collections import deque

def solution(skill, skill_trees):
    cnt = 0
    for s_t in skill_trees:
        skill_q = deque(list(skill))
        inorder = True
        for i in range(len(s_t)):
            if s_t[i] in skill_q:
                if s_t[i] != skill_q[0]:
                    inorder = False
                    break
                else:
                    skill_q.popleft()
        if inorder:
            cnt += 1
    answer = cnt
    return answer