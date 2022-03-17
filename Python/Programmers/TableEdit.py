from collections import deque
def solution(n, k, cmd):
    # 링크드 리스트
    data = [[i - 1, i + 1] for i in range(n)]
    # 양 끝은 링크 없음
    data[0][0] = -1
    data[-1][1] = -1
    answer = ['O' for _ in range(n)]
    
    stack = []
    cur_location = k
    for c in cmd:
        #print(cur_location)
        #print(c)
        #print("")
        #print("")
        if len(c) >= 2:
            # U, D
            cmd_type, num = c.split()
            if cmd_type == 'U':
                for _ in range(int(num)):
                    cur_location = data[cur_location][0]
            else:
                for _ in range(int(num)):
                    cur_location = data[cur_location][1]
        else:
            # C, Z
            if c == 'C':
                prev_, next_ = data[cur_location]
                stack.append((prev_, next_, cur_location))
                answer[cur_location] = 'X'
                # 맨 앞 경우
                if prev_ == -1:
                    data[next_][0] = -1
                    cur_location = next_
                # 맨 뒤 경우
                elif next_ == -1:
                    data[prev_][1] = -1
                    cur_location = prev_
                # 보통 경우
                else:
                    data[prev_][1] = next_
                    data[next_][0] = prev_
                    cur_location = next_
            else:
                prev_, next_, popped_idx = stack.pop()
                answer[popped_idx] = 'O'
                
                if popped_idx == 0:
                    data[next_][0] = popped_idx
                elif popped_idx == len(data) - 1:
                    data[prev_][1] = popped_idx
                else:
                    data[next_][0] = popped_idx
                    data[prev_][1] = popped_idx
                
    
    return ''.join(answer)