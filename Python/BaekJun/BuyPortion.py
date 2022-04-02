from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
portionCost = list(map(int, input().split()))
portionCost.insert(0, 0)
portionDiscount = [[] for _ in range(N + 1)]

INF = int(1e10)
answer = INF

for item in range(1, N + 1):
  n = int(input())
  for _ in range(n):
    a, d = map(int, input().split())
    portionDiscount[item].append((a, d))

for buy_order in permutations([item for item in range(1, N + 1)], N):
  tmpPortionCost = [cost for cost in portionCost]
  totalCost = 0
  for item in buy_order:
    totalCost += tmpPortionCost[item]
    for discount_item, discount_cost in portionDiscount[item]:
      tmpPortionCost[discount_item] -= discount_cost
      if tmpPortionCost[discount_item] <= 0:
        tmpPortionCost[discount_item] = 1
  answer = min(answer, totalCost)

print(answer)

