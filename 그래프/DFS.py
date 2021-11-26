def dfs(x, discoverd):
    discoverd.append(x)
    print(x, end=' ')

    for v in graph[x]:
        if v not in discoverd:
            dfs(v, discoverd)


graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}
dfs(1, [])