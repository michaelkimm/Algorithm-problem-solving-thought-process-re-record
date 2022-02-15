def solution(genres, plays):
    
    genres_played = {g:0 for g in set(genres)}
    d = {g:[] for g in set(genres)}
    for gen, cnt, num in zip(genres, plays, range(len(plays))):
        genres_played[gen] += cnt
        d[gen].append((cnt, num))
    
    answer = []
    genres_played_cnt_order = [k for k, v in sorted(genres_played.items(), reverse=True, key=lambda x: x[1])]
    for gen in genres_played_cnt_order:
        # 최대 플레이 곡 두개 삽입
        temp = [e[1] for e in sorted(d[gen], key=lambda x: (-x[0], x[1]))]
        answer += temp[:min(2, len(d[gen]))]
    
    return answer