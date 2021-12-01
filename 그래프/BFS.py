from collections import deque


def iterative_bfs(start, discovered=[]):
    discovered.append(start)
    q = deque([start])

    while q:
        v = q.popleft()
        for nv in graph[v]:
            if nv not in discovered:
                discovered.append(nv)
                q.append(nv)

    return discovered


graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

print(iterative_bfs(1))