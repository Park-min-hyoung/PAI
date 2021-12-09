#77

from itertools import combinations

# DFS로 k개 조합 생성
def dfs(element, idx, k):
    if k == 0:
        result.append(element[:])
        return

    for i in range(idx, n + 1):
        element.append(i)

        dfs(element, i + 1, k - 1)
        element.pop()


n = 4
k = 2

result = []
dfs([], 1, k)

print(result)

print(list(map(list, combinations(range(1, n + 1), k))))