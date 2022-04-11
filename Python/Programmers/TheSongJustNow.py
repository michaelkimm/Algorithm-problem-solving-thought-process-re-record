import re
def get_sequential_intesect_cnt(str1, str2):
    dp = [[0] * len(str2) for _ in range(len(str1))]
    max_cnt = 0
    for idx1 in range(len(str1)):
        for idx2 in range(len(str2)):
            val = 1 if str1[idx1] == str2[idx2] else 0
            dp[idx1][idx2] = dp[idx1 - 1][idx2 - 1] + val if idx1 - 1 >= 0 and idx2 - 1 >= 0 else val
            max_cnt = max(max_cnt, dp[idx1][idx2])
    return max_cnt
    
def time_str_to_min(time):
    hr, m = time.split(':')
    return int(hr) * 60 + int(m)

def str_notes_to_list(str_note):
    # A, A#, B, C, C#, D, D#, E, F, F#, G, G#
    result = re.findall('[A-Z]#?', str_note)
    return result
    
def solution(m, musicinfos):
    m = str_notes_to_list(m)
    candidates = []
    for idx, music_info in enumerate(musicinfos):
        start_time, end_time, title, content = music_info.split(',')
        start_time = time_str_to_min(start_time)
        end_time = time_str_to_min(end_time)
        content = str_notes_to_list(content)
        content_unit = content
        while (end_time - start_time) > len(content):
            content += content_unit
        content = content[:end_time - start_time]   
        common_cnt = get_sequential_intesect_cnt(m, content)
        if common_cnt == len(m):
            candidates.append((end_time - start_time, idx, title))
    answer = "(None)"
    if candidates:
        candidates.sort(key=lambda x:(-x[0], x[1]))
        answer = candidates[0][2]
    return answer




# ============================================ #

def time_str_to_min(time):
    hr, m = time.split(':')
    return int(hr) * 60 + int(m)

def sharp_to_lower_case(notes):
    return notes.replace('C#', 'c').replace('A#', 'a').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')

def solution(m, musicinfos):
    m = sharp_to_lower_case(m)
    candidates = []
    for idx, music_info in enumerate(musicinfos):
        start_time, end_time, title, content = music_info.split(',')
        start_time = time_str_to_min(start_time)
        end_time = time_str_to_min(end_time)
        content = sharp_to_lower_case(content)
        content_unit = content
        while (end_time - start_time) > len(content):
            content += content_unit
        content = content[:end_time - start_time]   
        if m in content:
            candidates.append((end_time - start_time, idx, title))
    answer = "(None)"
    if candidates:
        candidates.sort(key=lambda x:(-x[0], x[1]))
        answer = candidates[0][2]
    return answer