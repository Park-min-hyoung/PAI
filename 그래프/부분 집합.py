#78

def dfs():
    for num in nums:
        if prev_n[-1] and num <= prev_n[-1][-1]:
            continue

        next_value = prev_n[-1] + [num]
        prev_n.append(next_value[:])

        if next_value not in result:
            result.append(next_value[:])
            dfs()
            prev_n.pop()


nums = [1, 2, 3]
result = [[]]
prev_n = [[]]

dfs()

print(result)