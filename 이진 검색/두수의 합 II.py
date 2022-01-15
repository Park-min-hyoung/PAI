#167

import bisect

numbers = [2, 3, 6]
target = 6


result = []
for idx, num in enumerate(numbers):
    find_num = target - num
    find_idx = bisect.bisect_left(numbers, find_num)
    if find_idx < len(numbers) and find_num == numbers[find_idx]:
        if idx == find_idx:
            continue
        result.append(find_idx + 1)
        result.append(idx + 1)
        break

print(sorted(result))