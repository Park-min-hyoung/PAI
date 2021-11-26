# 347

import collections

nums = [1, 2]
k = 2

nums_dict = collections.defaultdict(int)
for num in nums:
    nums_dict[num] += 1
nums_dict = sorted(nums_dict.items(), key=lambda x: (-x[1]))

result = []
for i in range(k):
    result.append(nums_dict[i][0])

print(result)