#77

def dfs(arr):
    if len(prev_v) == k:
        result.append(prev_v[:])

    for num in arr:
        if prev_v and prev_v[-1] > num:
            continue
        next_v = arr[:]
        next_v.remove(num)

        prev_v.append(num)
        dfs(next_v)
        prev_v.pop()


n = 1
k = 1

li = list(x for x in range(1, n + 1))
prev_v = []
result = []

dfs(li)
print(result)