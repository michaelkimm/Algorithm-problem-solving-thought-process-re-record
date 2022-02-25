used = []
ticket_dict = {}
sequences = []

def my_dfs(stack, tickets, s, e):
    global ticket_dict, used, sequences
    used[ticket_dict[(s, e)]] -= 1
    stack.append((s, e))
    # print(stack)
    
    all_used = True
    for ticket_use in used:
        if ticket_use > 0:
            all_used = False
            break
    if all_used:
        tmp = ['ICN']
        for u, v in stack:
          tmp.append(v)
        sequences.append(tmp)
        return
    
    for u, v in tickets:
        if u == e and used[ticket_dict[(u, v)]] > 0:
            my_dfs(stack, tickets, u, v)
            used[ticket_dict[(u, v)]] += 1
            if len(stack) > 0:
              stack.pop()
        
def solution(tickets):
    global ticket_dict, used, sequences

    ticket_set = set([(u, v) for u, v in tickets])
    for i, ticket in enumerate(list(ticket_set)):
        ticket_dict[(ticket[0], ticket[1])] = i
        
    
    used = [0] * len(ticket_dict)
    for u, v in tickets:
      used[ticket_dict[(u, v)]] += 1
      
    stack = []
    
    for u, v in tickets:
        if u == "ICN":
            my_dfs(stack, tickets, u, v)
            used[ticket_dict[(u, v)]] += 1
            if len(stack) > 0:  
              stack.pop()
    # 방문한 곳에서 다른 곳으로 갈 티켓 없는 경우
    # print(sequences)
    return sorted(sequences)[0]



# ============================================================ #
from collections import defaultdict

def solution(tickets):
    ticket_dict = defaultdict(list)
    for u, v in tickets:
        ticket_dict[u].append(v)
        
    for key in ticket_dict.keys():
        ticket_dict[key].sort(reverse=True)
        
    stack = ["ICN"]
    path = []
    
    while stack:
        site = stack[-1]
        if ticket_dict[site] == []:
            path.append(stack.pop())
        else:
            stack.append(ticket_dict[site].pop())
    
    return path[::-1]