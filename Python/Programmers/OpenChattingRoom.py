def solution(records):
    nick_dict = {}
    # 최종 닉네임
    for record in records:
        record_split = record.split()
        if len(record_split) >= 3:
            nick_dict[record_split[1]] = record_split[2]
    
    answer = []
    # 결과
    for record in records:
        record_split = record.split()
        if record_split[0] == "Enter":
            answer.append(nick_dict[record_split[1]] + "님이 들어왔습니다.")
        elif record_split[0] == "Leave":
            answer.append(nick_dict[record_split[1]] + "님이 나갔습니다.")
    
    return answer