def check_dist_right(ary, i0, j0, i1, j1):
    if abs(i0 - i1) == 0 or abs(j0 - j1) == 0:
        if ary[(i0 + i1) // 2][(j0 + j1) // 2] == 'X':
            return True
        else:
            return False
    else:
        if ary[i1][j0] == 'X' and ary[i0][j1] == 'X':
            return True
        else:
            return False
        
def surf_ary(place):
    for i in range(len(place)):
        for j in range(len(place)):
            for cmpi in range(len(place)):
                for cmpj in range(len(place)):
                    dist = abs(i - cmpi) + abs(j - cmpj)
                    if dist <=2 and place[i][j] == "P" and place[cmpi][cmpj] == "P":
                        if dist == 1:
                            # 안지킴
                            return 0
                        elif dist == 2 and not check_dist_right(place, i, j, cmpi, cmpj):
                            # 안지킴
                            return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(surf_ary(place))
    return answer