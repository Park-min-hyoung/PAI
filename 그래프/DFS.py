# 재귀를 이용한 DFS
def recursive_dfs(v, discovered=[]):
    discovered.append(v)

    for x in graph[v]:
        if x not in discovered:
            recursive_dfs(x, discovered)

    return discovered

def iterative_dfs(v, discovered=[]):
    stack = [v]

    while stack:
        x = stack.pop()
        if x not in discovered:
            discovered.append(x)
            for value in graph[x]:
                stack.append(value)

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

print(recursive_dfs(1))
print(iterative_dfs(1))