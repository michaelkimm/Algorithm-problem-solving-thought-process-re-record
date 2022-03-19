from collections import deque
import heapq

def waiting_to_work(working_hp, read_q, write_q, cur_time):
    if not working_hp and write_q:
        process = write_q.popleft()
        process = (process[0] + cur_time, process[1], process[2], process[3], process[4])
        heapq.heappush(working_hp, process)
    else:
        while read_q:
            process = read_q.popleft()
            process = (process[0] + cur_time, process[1], process[2], process[3])
            heapq.heappush(working_hp, process)

def update_waiting_list(processes, read_list, write_list, cur_time, past_popped_idx):
    popped_idx = past_popped_idx
    for idx in range(past_popped_idx + 1, len(processes)):
        process = processes[idx]
        data = process.split()
        t1 = int(data[1])
        t2 = int(data[2])
        if t1 > cur_time:
            break
        popped_idx = idx
        if process[0] == 'r':
            _, _, _, start, end = process.split()
            read_list.append((t2, 'r', int(start), int(end)))
        else:
            # 쓰기 경우
            _, _, _, start, end, ch = process.split()
            write_list.append((t2, 'w', int(start), int(end), ch))

    return popped_idx

def check_work_done(cur_time, working_hp, done_process_cnt, answer, arr):
    if not working_hp:
        return done_process_cnt, False
    
    while working_hp and int(working_hp[0][0]) <= cur_time:
        process = heapq.heappop(working_hp)
        if process[1] == 'r':
            end_time, _, start, end = process[0], process[1], process[2], process[3]
            answer.append(''.join(arr[start:end + 1]))
        elif process[1] == 'w':
            end_time, _, start, end, ch = process[0], process[1], process[2], process[3], process[4]
            for idx in range(start, end + 1):
                arr[idx] = ch
        done_process_cnt += 1
    return done_process_cnt, True

def solution(arr, processes):
    answer = []
    read_q = deque([])
    write_q = deque([])
    working_hp = []
    cur_time = 0
    past_popped_idx = -1
    done_process_cnt = 0
    not_worked_time = 0

    while done_process_cnt <= len(processes) - 1:
        cur_time += 1
        done_process_cnt, worked = check_work_done(cur_time, working_hp, done_process_cnt, answer, arr)
        if not worked:
          not_worked_time += 1
        past_popped_idx = update_waiting_list(processes, read_q, write_q, cur_time, past_popped_idx)

        if working_hp:
            if working_hp[0][1] != 'r':
                continue
            else:
                if write_q:
                    continue
            
        waiting_to_work(working_hp, read_q, write_q, cur_time)
    answer.append(str(cur_time - not_worked_time))
    return answer
    