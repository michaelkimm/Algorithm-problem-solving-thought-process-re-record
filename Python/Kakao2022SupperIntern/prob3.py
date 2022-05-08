"""
문제 설명
[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]

당신은 코딩 테스트를 준비하기 위해 공부하려고 합니다. 코딩 테스트 문제를 풀기 위해서는 알고리즘에 대한 지식과 코드를 구현하는 능력이 필요합니다.

알고리즘에 대한 지식은 알고력, 코드를 구현하는 능력은 코딩력이라고 표현합니다. 알고력과 코딩력은 0 이상의 정수로 표현됩니다.

문제를 풀기 위해서는 문제가 요구하는 일정 이상의 알고력과 코딩력이 필요합니다.

예를 들어, 당신의 현재 알고력이 15, 코딩력이 10이라고 가정해보겠습니다.

A라는 문제가 알고력 10, 코딩력 10을 요구한다면 A 문제를 풀 수 있습니다.
B라는 문제가 알고력 10, 코딩력 20을 요구한다면 코딩력이 부족하기 때문에 B 문제를 풀 수 없습니다.
풀 수 없는 문제를 해결하기 위해서는 알고력과 코딩력을 높여야 합니다. 알고력과 코딩력을 높이기 위한 다음과 같은 방법들이 있습니다.

알고력을 높이기 위해 알고리즘 공부를 합니다. 알고력 1을 높이기 위해서 1의 시간이 필요합니다.
코딩력을 높이기 위해 코딩 공부를 합니다. 코딩력 1을 높이기 위해서 1의 시간이 필요합니다.
현재 풀 수 있는 문제 중 하나를 풀어 알고력과 코딩력을 높입니다. 각 문제마다 문제를 풀면 올라가는 알고력과 코딩력이 정해져 있습니다.
문제를 하나 푸는 데는 문제가 요구하는 시간이 필요하며 같은 문제를 여러 번 푸는 것이 가능합니다.
당신은 주어진 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단시간을 구하려 합니다.

초기의 알고력과 코딩력을 담은 정수 alp와 cop, 문제의 정보를 담은 2차원 정수 배열 problems가 매개변수로 주어졌을 때, 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단시간을 return 하도록 solution 함수를 작성해주세요.

모든 문제들을 1번 이상씩 풀 필요는 없습니다.

제한사항
초기의 알고력을 나타내는 alp와 초기의 코딩력을 나타내는 cop가 입력으로 주어집니다.
0 ≤ alp,cop ≤ 150
1 ≤ problems의 길이 ≤ 100
problems의 원소는 [alp_req, cop_req, alp_rwd, cop_rwd, cost]의 형태로 이루어져 있습니다.
alp_req는 문제를 푸는데 필요한 알고력입니다.
0 ≤ alp_req ≤ 150
cop_req는 문제를 푸는데 필요한 코딩력입니다.
0 ≤ cop_req ≤ 150
alp_rwd는 문제를 풀었을 때 증가하는 알고력입니다.
0 ≤ alp_rwd ≤ 30
cop_rwd는 문제를 풀었을 때 증가하는 코딩력입니다.
0 ≤ cop_rwd ≤ 30
cost는 문제를 푸는데 드는 시간입니다.
1 ≤ cost ≤ 100
입출력 예
alp	cop	problems	result
10	10	[[10,15,2,1,2],[20,20,3,3,4]]	15
0	0	[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]	13
입출력 예 설명
입출력 예 #1

코딩력 5를 늘립니다. 알고력 10, 코딩력 15가 되며 시간이 5만큼 소요됩니다.
1번 문제를 5번 풉니다. 알고력 20, 코딩력 20이 되며 시간이 10만큼 소요됩니다. 15의 시간을 소요하여 모든 문제를 풀 수 있는 알고력과 코딩력을 가질 수 있습니다.
입출력 예 #2

1번 문제를 2번 풉니다. 알고력 4, 코딩력 2가 되며 시간이 4만큼 소요됩니다.
코딩력 3을 늘립니다. 알고력 4, 코딩력 5가 되며 시간이 3만큼 소요됩니다.
2번 문제를 2번 풉니다. 알고력 10, 코딩력 7이 되며 시간이 4만큼 소요됩니다.
4번 문제를 1번 풉니다. 알고력 10, 코딩력 11이 되며 시간이 2만큼 소요됩니다. 13의 시간을 소요하여 모든 문제를 풀 수 있는 알고력과 코딩력을 가질 수 있습니다.
제한시간 안내

정확성 테스트 : 10초
효율성 테스트 : 언어별로 작성된 정답 코드의 실행 시간의 적정 배수
"""

from collections import deque
import heapq

def solution(alp, cop, problems):
    maxAlpNeeded = 0
    maxCopNeeded = 0
    probables = []
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        maxAlpNeeded = max(maxAlpNeeded, alp_req)
        maxCopNeeded = max(maxCopNeeded, cop_req)
        if alp >= alp_req and cop >= cop_req:
            probables.append([alp_req, cop_req, alp_rwd, cop_rwd, cost])
    
    
    # bfs
    timePassed = 0
    node = (timePassed, alp, cop)
    visited = set([(timePassed, alp, cop)])
    hp = [node]
    heapq.heapify(hp)
    answer = 0
    while hp:
        timePassed, cur_alp, cur_cop = heapq.heappop(hp)
        if cur_alp >= maxAlpNeeded and cur_cop >= maxCopNeeded:
            # print("we got answer!")
            answer = timePassed
            break
        # 알고력 + 1
        if not (cur_alp + 1, cur_cop) in visited:
            heapq.heappush(hp, (timePassed + 1, cur_alp + 1, cur_cop))
            visited.add((cur_alp + 1, cur_cop))
        # 코딩력 + 1
        if not (cur_alp, cur_cop + 1) in visited:
            heapq.heappush(hp, (timePassed + 1, cur_alp, cur_cop + 1))
            visited.add((cur_alp, cur_cop + 1))
        # 문제 풀기
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp_req > cur_alp or cop_req > cur_cop:
                continue
            if not (timePassed + cost, cur_alp + alp_rwd, cur_cop + cop_rwd) in visited:
                heapq.heappush(hp, (timePassed + cost, cur_alp + alp_rwd, cur_cop + cop_rwd))
                visited.add((timePassed + cost, cur_alp + alp_rwd, cur_cop + cop_rwd))
    # print(maxAlpNeeded, maxCopNeeded)
    return answer


# ====================================================================

from collections import deque
import heapq

def solution(alp, cop, problems):
    maxAlpNeeded = 0
    maxCopNeeded = 0
    probables = []
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        maxAlpNeeded = max(maxAlpNeeded, alp_req)
        maxCopNeeded = max(maxCopNeeded, cop_req)
        if alp >= alp_req and cop >= cop_req:
            probables.append([alp_req, cop_req, alp_rwd, cop_rwd, cost])


    # bfs
    timePassed = 0
    node = (timePassed, alp, cop)
    visited = set([(timePassed, alp, cop)])
    hp = [node]
    heapq.heapify(hp)
    answer = 0
    while hp:
        timePassed, cur_alp, cur_cop = heapq.heappop(hp)
        if cur_alp >= maxAlpNeeded and cur_cop >= maxCopNeeded:
            # print("we got answer!")
            answer = timePassed
            break
        # 알고력 + 1
        if not (cur_alp + 1, cur_cop) in visited:
            heapq.heappush(hp, (timePassed + 1, cur_alp + 1, cur_cop))
            visited.add((cur_alp + 1, cur_cop))
        # 코딩력 + 1
        if not (cur_alp, cur_cop + 1) in visited:
            heapq.heappush(hp, (timePassed + 1, cur_alp, cur_cop + 1))
            visited.add((cur_alp, cur_cop + 1))
        # 문제 풀기
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp_req > cur_alp or cop_req > cur_cop:
                continue
            if not (timePassed + cost, cur_alp + alp_rwd, cur_cop + cop_rwd) in visited:
                heapq.heappush(hp, (timePassed + cost, cur_alp + alp_rwd, cur_cop + cop_rwd))
                visited.add((timePassed + cost, cur_alp + alp_rwd, cur_cop + cop_rwd))
    # print(maxAlpNeeded, maxCopNeeded)
    return answer

    
# ====================================================================

# 시험 이후 수정본

from collections import deque
import heapq

def solution(alp, cop, problems):
    maxAlpNeeded = 0
    maxCopNeeded = 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        maxAlpNeeded = max(maxAlpNeeded, alp_req)
        maxCopNeeded = max(maxCopNeeded, cop_req)

    # bfs
    timePassed = 0
    node = (timePassed, alp, cop)
    visited = set([(alp, cop)])
    hp = [node]
    heapq.heapify(hp)
    answer = 0
    while hp:
        timePassed, cur_alp, cur_cop = heapq.heappop(hp)

        # 방문 여부 확인
        if not (cur_alp, cur_cop) in visited:
            visited.add((cur_alp, cur_cop))
        else:
            continue
        
        # 탈출 조건
        if cur_alp >= maxAlpNeeded and cur_cop >= maxCopNeeded:
            # print("we got answer!")
            answer = timePassed
            break

        # 알고력 + 1
        heapq.heappush(hp, (timePassed + 1, cur_alp + 1, cur_cop))
        # 코딩력 + 1
        heapq.heappush(hp, (timePassed + 1, cur_alp, cur_cop + 1))
        # 문제 풀기
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp_req > cur_alp or cop_req > cur_cop:
                continue
            heapq.heappush(hp, (timePassed + cost, cur_alp + alp_rwd, cur_cop + cop_rwd))
    # print(maxAlpNeeded, maxCopNeeded)
    return answer