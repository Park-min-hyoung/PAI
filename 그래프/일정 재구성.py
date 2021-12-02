#322
from collections import defaultdict

def dfs(target, discovered=[]):
    discovered.append(target)

    for i, v in enumerate(ticket_dic[target]):
        next_n = ticket_dic[target][i]
        if v in ticket_dic or len(ticket_dic[target]) == 1:
            ticket_dic[target].remove(next_n)
            print(ticket_dic)
            print()
            dfs(v, discovered)

    return discovered


tickets = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],
           ["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],
           ["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
tickets.sort()
ticket_dic = defaultdict(list)

for ticket in tickets:
    ticket_dic[ticket[0]].append(ticket[1])
print(ticket_dic)

print(dfs('JFK'))

# 틀렸음