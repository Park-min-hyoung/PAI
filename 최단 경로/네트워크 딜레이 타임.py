#743

from collections import defaultdict
from collections import deque

def bfs(v, discovered, time):
    discovered.append(v)
    q = deque([(v, 0)])

    while q:
        nv = q.popleft()
        for next_v in time_dic[nv[0]]:
            time_v = next_v[1] + nv[1]
            q.append((next_v[0], time_v))
            time.append((next_v[0], time_v))
        time_dic[nv[0]] = []

    return sorted(time, key=lambda x:(-x[1]))


times = [[1,2,1],[2,1,3]]
n = 2
k = 2

time_dic = defaultdict(list)
for t in times:
    time_dic[t[0]].append((t[1], t[2]))
time = []

result = bfs(k, [], time)

if len(result) >= n - 1:
    target = result[0][0]
    value = result[0][1]
    for i in range(1, len(result)):
        if target == result[i][0] and value > result[i][1]:
            value = result[i][1]
    print(value)
else:
    print(-1)

# 틀렸음