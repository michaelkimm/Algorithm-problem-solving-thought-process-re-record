import heapq

INF = int(1e10)

def getTimeByRide(ride_times, walk_times, m):

    result = []

    distance = [[INF for _ in range(m + 1)] for _ in range(len(ride_times))]
    hp = []
    if ride_times[0] != -1:
        # 운전해서 시작한 경우
        heapq.heappush(hp, (ride_times[0], 0, 0))
        if ride_times[0] < distance[0][0]:
            distance[0][0] = ride_times[0]
    # 걷기로 시작한 경우
    heapq.heappush(hp, (walk_times[0], walk_times[0], 0))   
    if walk_times[0] < distance[0][walk_times[0]]:
        distance[0][walk_times[0]] = walk_times[0]
    # distance 업데이트

    while hp:
        cur_consumed_time, cur_conseq_walk_time, last_walked_road = heapq.heappop(hp)
        next_road = last_walked_road + 1
        # distance에 의한 조건 처리
        if distance[last_walked_road][cur_conseq_walk_time] < cur_consumed_time:
            continue

        # 다음 road 선택 (간선)
        if next_road >= len(ride_times):
            result.append(cur_consumed_time)
            continue
        # 탈 것 이용
        if ride_times[next_road] != -1:
            next_consumed_time = cur_consumed_time + ride_times[next_road]
            if next_consumed_time < distance[next_road][cur_conseq_walk_time]:
                distance[next_road][cur_conseq_walk_time] = next_consumed_time
                byRide = (next_consumed_time, 0, next_road)
                heapq.heappush(hp, byRide)
        # 도보 이용
        next_conseq_walk_time = cur_conseq_walk_time + walk_times[next_road]
        if next_conseq_walk_time > m:
            continue
        next_consumed_time = cur_consumed_time + walk_times[next_road]
        if next_consumed_time < distance[next_road][next_conseq_walk_time]:
            distance[next_road][next_conseq_walk_time] = next_consumed_time
            byWalk = (next_consumed_time, next_conseq_walk_time, next_road)
            heapq.heappush(hp, byWalk)

    return min(result) if result else INF

def solution(infos, m):
    N = len(infos)
    car_times = []
    bike_times = []
    public_times = []
    walk_times = []
    for info in infos:
        car_time, bike_time, public_time, walk_time = info
        car_times.append(car_time)
        bike_times.append(bike_time)
        public_times.append(public_time)
        walk_times.append(walk_time)

    # 자동차 소요 시간
    time_by_only_car = sum(car_times)
    # 자전거 소요 시간
    time_by_bike = getTimeByRide(bike_times, walk_times, m)
    # 대중교통 소요 시간
    time_by_public = getTimeByRide(public_times, walk_times, m)
    # 도보 소요 시간
    time_by_only_walk = sum(walk_times) if sum(walk_times) <= m else INF
    answer = min([time_by_only_car, time_by_bike, time_by_public, time_by_only_walk])
    return answer