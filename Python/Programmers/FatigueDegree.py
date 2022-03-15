import itertools

def solution(k, dungeons):
    indexes = [i for i in range(len(dungeons))]
    dungeon_orders = list(itertools.permutations(indexes, len(dungeons)))
    
    max_traveled = 0
    for dungeon_order in dungeon_orders:
        current_fatigue = k
        traveled_cnt = 0
        for idx in dungeon_order:
            min_needed = dungeons[idx][0]
            consumption = dungeons[idx][1]
            if min_needed > current_fatigue:
                break
            current_fatigue -= consumption
            traveled_cnt += 1
        max_traveled = max(max_traveled, traveled_cnt)
            
    return max_traveled