from bisect import bisect_left, bisect_right

class KeyifyList(object):
    def __init__(self, inner, key):
        self.inner = inner
        self.key = key

    def __len__(self):
        return len(self.inner)

    def __getitem__(self, k):
        return self.key(self.inner[k])


def get_total_adv_played(logs, adv_start, adv_end):
    adv_seen_time = 0
    for log in logs:
        s_log, e_log = log[0], log[1]
        if  e_log >= adv_end:
            if s_log <= adv_start:
                adv_seen_time += (adv_end - adv_start)
            else:
                adv_seen_time += (adv_end - e_log)
        else:
            if adv_start <= s_log:
                adv_seen_time += (e_log - s_log)
            else:
                adv_seen_time += (e_log - adv_start)
    return adv_seen_time

def get_sec_from_log(log):
    tmp_log = log.split(':')
    sec =  int(tmp_log[0]) * 3600 + int(tmp_log[1]) * 60 + int(tmp_log[2])
    return sec
def get_log_from_sec(sec):
    answer_h = sec // 3600
    answer_m = (sec % 3600) // 60
    answer_s = (sec % 3600) % 60
    return str(answer_h).zfill(2) + ':' + str(answer_m).zfill(2) + ':' + str(answer_s).zfill(2)

def solution(play_time, adv_time, logs):
    sec_logs = []
    play_time_sec = get_sec_from_log(play_time)
    adv_time_sec = get_sec_from_log(adv_time)
    for log in logs:
        start_log, end_log = log.split('-')
        start_time = get_sec_from_log(start_log)
        end_time = get_sec_from_log(end_log)
        sec_logs.append((start_time, end_time))
        
    end_sorted_logs = sorted(sec_logs, key=lambda x:x[1])
    start_sorted_logs = sorted(sec_logs)
    answer_start, answer_played = 0, 0
    # 시작 시간 정렬
    for s_sec, e_sec in start_sorted_logs:
        target_start, target_end = s_sec, s_sec + adv_time_sec
        # 경계 처리
        if target_end > play_time_sec:
            continue
        print("te:", target_end, "pts:", play_time_sec)
        target_logs = []
        # 타겟 시작 시간 보다 빨리 끝나는 로그 제외
        left_idx = bisect_left(KeyifyList(end_sorted_logs, key=lambda x: x[1]), target_start)
        # 타겟 끝 시간 보다 늦게 시작하는 로그 제외
        right_idx = bisect_right(KeyifyList(start_sorted_logs, key=lambda x: x[0]), target_end)
        if left_idx > right_idx:
            continue
        total_adv_played_time = get_total_adv_played(start_sorted_logs[left_idx:right_idx], target_start, target_end)
        
        if answer_played < total_adv_played_time:
            print("ap:", answer_played, "tapt:", total_adv_played_time)
            answer_played = total_adv_played_time
            answer_start = target_start
    print("==")
    # 끝시간 맞춤
    for s_sec, e_sec in end_sorted_logs:
        target_start, target_end = e_sec - adv_time_sec, e_sec
        # 경계 처리
        if target_start < 0:
            continue
        print(get_log_from_sec(target_start))
        target_logs = []
        # 타겟 시작 시간 보다 빨리 끝나는 로그 제외
        left_idx = bisect_left(KeyifyList(end_sorted_logs, key=lambda x: x[1]), target_start)
        # 타겟 끝 시간 보다 늦게 시작하는 로그 제외
        right_idx = bisect_right(KeyifyList(start_sorted_logs, key=lambda x: x[0]), target_end)
        if left_idx > right_idx:
            continue
        total_adv_played_time = get_total_adv_played(start_sorted_logs[left_idx:right_idx], target_start, target_end)
        
        if answer_played < total_adv_played_time:
            print("ap:", answer_played, "tapt:", total_adv_played_time)
            answer_played = total_adv_played_time
            answer_start = target_start
    
    return get_log_from_sec(answer_start)



# ============================================================= #

def get_sec_from_log(log):
    tmp_log = log.split(':')
    sec =  int(tmp_log[0]) * 3600 + int(tmp_log[1]) * 60 + int(tmp_log[2])
    return sec

def solution(play_time, adv_time, logs):
    play_time_sec = get_sec_from_log(play_time)
    adv_time_sec = get_sec_from_log(adv_time)
    dp = [0] * (play_time_sec + 1)
    for log in logs:
        start_log, end_log = log.split('-')
        start_time = get_sec_from_log(start_log)
        end_time = get_sec_from_log(end_log)
        dp[start_time] += 1
        dp[end_time] -= 1
        
    for i in range(1, len(dp)):
        # 현재 구간 시청자 수
        dp[i] = dp[i] + dp[i - 1]
    for i in range(1, len(dp)):
        # 누적 시청자 수
        dp[i] = dp[i] + dp[i - 1]
    
    max_played = 0
    min_time = play_time_sec - adv_time_sec
    for t in range(adv_time_sec - 1, play_time_sec):
        if t >= adv_time_sec:
            if dp[t] - dp[t - adv_time_sec] > max_played:
                max_played = dp[t] - dp[t - adv_time_sec]
                min_time = t - adv_time_sec + 1
        else:
            max_played = dp[adv_time_sec - 1]
            min_time = 0
    
    return get_log_from_sec(min_time)