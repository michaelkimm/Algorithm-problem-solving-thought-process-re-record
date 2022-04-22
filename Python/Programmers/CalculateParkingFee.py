from collections import defaultdict
import math

def time_str_to_min(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)

def get_additional_fee(parked_amount_time, default_time, time_unit, fee_unit):
    result = 0
    if parked_amount_time > default_time:
        d_time = parked_amount_time - default_time
        result += math.ceil(d_time / time_unit) * fee_unit
    return result

def solution(fees, records):
    default_time, default_fee, time_unit, fee_unit = fees
    entrance_time_dict = defaultdict(list)
    exit_time_dict = defaultdict(list)
    fee_dict = defaultdict(int)
    answer = []
    for record in records:
        time_str, car_num, order = record.split()
        time_min = time_str_to_min(time_str)
        if order == "IN":
            entrance_time_dict[car_num].append(time_min)
        else:
            exit_time_dict[car_num].append(time_min)
            
    # 누적 주차 시간 계산
    for car_num in entrance_time_dict.keys():
        # 마지막이 출차인 경우
        if len(entrance_time_dict[car_num]) == len(exit_time_dict[car_num]):
            total_parked_time = 0
            for idx in range(len(entrance_time_dict[car_num])):
                total_parked_time += exit_time_dict[car_num][idx] - entrance_time_dict[car_num][idx]
        # 마지막이 입차인 경우
        else:
            total_parked_time = 0
            for idx in range(len(exit_time_dict[car_num])):
                total_parked_time += exit_time_dict[car_num][idx] - entrance_time_dict[car_num][idx]
            total_parked_time += time_str_to_min("23:59") - entrance_time_dict[car_num][-1]
            
        # 요금 계산
        fee_dict[car_num] += default_fee
        fee_dict[car_num] += get_additional_fee(total_parked_time, default_time, time_unit, fee_unit)
            
    
    for car_num in fee_dict.keys():
        answer.append((car_num, fee_dict[car_num]))
    # 차량 번호가 작은 자동차부터
    answer.sort()
    return [fee for car_num, fee in answer]