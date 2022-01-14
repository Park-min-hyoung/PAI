#167

import bisect

numbers = [-1, 0]
target = -1


result = []
for idx, num in enumerate(numbers):
    find_num = target - num
    find_idx = bisect.bisect_left(numbers, find_num)
    if find_idx < len(numbers) and find_num == numbers[find_idx]:
        if idx == find_idx and idx + 1 < len(numbers) and numbers[idx] != numbers[idx + 1]:
            continue
        result.append(idx + 1)

print(result)