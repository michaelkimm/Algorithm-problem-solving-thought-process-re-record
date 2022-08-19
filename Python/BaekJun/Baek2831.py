import sys
input = sys.stdin.readline

def getMaxPairCnt(peopleWhoWantTaller, peopleWhoWantShorter):
    peopleWhoWantTaller.sort()
    peopleWhoWantShorter.sort()

    cnt = 0
    p1 = 0
    p2 = 0
    while p1 < len(peopleWhoWantTaller) and p2 < len(peopleWhoWantShorter):

        p1Height = peopleWhoWantTaller[p1]
        p2Height = peopleWhoWantShorter[p2]
        if p1Height < p2Height:
            cnt += 1
            p1 += 1
            p2 += 1
        elif (p1Height == p2Height) or (p1Height > p2Height):
            p2 += 1

    return cnt

N = int(input())
boys = list(map(int, input().split()))
girls = list(map(int, input().split()))

boysWhoWantLittleGirl = []
boysWhoWnatTallerGirl = []

girlsWhoWantLittleBoy = []
girlsWhoWnatTallerBoy = []

for boy in boys:
    if boy > 0:
        boysWhoWnatTallerGirl.append(boy)
    else:
        boysWhoWantLittleGirl.append(abs(boy))

for girl in girls:
    if girl > 0:
        girlsWhoWnatTallerBoy.append(girl)
    else:
        girlsWhoWantLittleBoy.append(abs(girl))


answer = getMaxPairCnt(boysWhoWnatTallerGirl, girlsWhoWantLittleBoy) + getMaxPairCnt(girlsWhoWnatTallerBoy, boysWhoWantLittleGirl)

print(answer)