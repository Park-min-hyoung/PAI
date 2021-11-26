#200

def dfs(x, y):
    check[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if not check[nx][ny] and grid[nx][ny] == '1':
                dfs(nx, ny)

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

m = n = 0
check = []
for gr in grid:
    check.append([0] * len(gr))
    m += 1
    n = len(gr)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
for i in range(m):
    for j in range(n):
        if not check[i][j] and grid[i][j] == '1':
            dfs(i, j)
            result += 1

print(result)