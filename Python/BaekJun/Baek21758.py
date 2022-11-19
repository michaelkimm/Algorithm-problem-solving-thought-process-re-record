import sys
input = sys.stdin.readline

N = int(input().strip())
honeys = list(map(int, input().split()))

def solution(honeys):
    if len(honeys) == 3:
        return max(honeys) * 2
    # Case 1 : 통벌벌, 꿀통을 맨 끝에 두는 경우
    # 양 끝 꿀통 중, 더 큰 꿀이 담긴 곳을 꿀통으로 지정.
    # 꿀 통을 맨 마지막에 위치 시키게 배열 재연산

    # 시작 지점을 꿀벌1로 지정
    bee1 = 0
    bee2 = 1
    # 다른 끝 다음 부터 시작해서 총합 계산
    bee1TotalWithBee2 = sum(honeys) - honeys[bee1]
    bee2Total = bee1TotalWithBee2 - 2 * honeys[bee2]
    maxTotal = bee1TotalWithBee2 + bee2Total
    for bee2 in range(2, len(honeys)):
        bee2Total += honeys[bee2 - 1]
        bee2Total -= (2 * honeys[bee2])
        maxTotal = max(maxTotal, bee1TotalWithBee2 + bee2Total)

    honeys.reverse()

    # Case 2 : 벌벌통, 꿀통을 맨 끝에 두는 경우
    # 시작 지점을 꿀벌1로 지정
    bee1 = 0
    bee2 = 1
    # 다른 끝 다음 부터 시작해서 총합 계산
    bee1TotalWithBee2 = sum(honeys) - honeys[bee1]
    bee2Total = bee1TotalWithBee2 - 2 * honeys[bee2]
    maxTotal = max(maxTotal, bee1TotalWithBee2 + bee2Total)
    for bee2 in range(2, len(honeys)):
        bee2Total += honeys[bee2 - 1]
        bee2Total -= (2 * honeys[bee2])
        maxTotal = max(maxTotal, bee1TotalWithBee2 + bee2Total)

    # Case 3 : 꿀통을 중간에 두는 경우
    case2Total = sum(honeys) - honeys[0] - honeys[-1] + max(honeys[1:-1])
    maxTotal = max(case2Total, maxTotal)
    return maxTotal


print(solution(honeys))