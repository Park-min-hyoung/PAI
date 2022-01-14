#349

import bisect

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
nums2.sort()

result = []
for value in set(nums1):
    idx = bisect.bisect_left(nums2, value)
    if value == nums2[idx]:
        result.append(value)

print(result)