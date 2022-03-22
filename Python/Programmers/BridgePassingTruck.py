from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    waiting_q = deque(truck_weights)
    passing_q1 = deque([])
    passing_q2 = deque([])
    passing_bus_weight = 0
    passed = []
    
    while waiting_q or passing_q1 or passing_q2:
        time_passed = False
        # 트럭 지나간 정도 업데이트
        if passing_q1:
            time += 1
            time_passed = True
            while passing_q1:
                t_weight, time_left = passing_q1.popleft()
                if time_left == 1:
                    # 탈출!
                    passed.append(t_weight)
                    passing_bus_weight -= t_weight
                else:
                    passing_q2.append((t_weight, time_left - 1))
        elif passing_q2:
            time += 1
            time_passed = True
            while passing_q2:
                t_weight, time_left = passing_q2.popleft()
                if time_left == 1:
                    # 탈출!
                    passed.append(t_weight)
                    passing_bus_weight -= t_weight
                else:
                    passing_q1.append((t_weight, time_left - 1))
        
        # 기다리는 트럭 -> 지나가는 트럭
        if waiting_q and waiting_q[0] + passing_bus_weight <= weight:
            t_weight = waiting_q.popleft()
            if passing_q1:
                passing_q1.append((t_weight, bridge_length))
            else:
                passing_q2.append((t_weight, bridge_length))
            passing_bus_weight += t_weight
            if not time_passed:
                time += 1
        
    return time