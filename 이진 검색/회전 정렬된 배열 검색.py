#33
import bisect

nums = [1]
target = 0

idx = nums.index(min(nums))
nums1 = nums[0:idx]
nums2 = nums[idx:]

if nums1 and target >= nums1[0]:
    find_idx = bisect.bisect_left(nums1, target)
    if find_idx >= len(nums1) or target != nums1[find_idx]:
        find_idx = -1
else:
    find_idx = bisect.bisect_left(nums2, target)
    if find_idx >= len(nums2) or target != nums2[find_idx]:
        find_idx = -1
    find_idx += len(nums1)

print(find_idx)