#75
def qucikSort(num, lo, hi):
    def partition(lo, hi):
        pivot = nums[hi]
        left = lo

        for right in range(lo, hi):
            if nums[right] < pivot:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        nums[left], nums[hi] = nums[hi], nums[left]

        return left

    if lo < hi:
        part = partition(lo, hi)
        qucikSort(nums, lo, part - 1)
        qucikSort(nums, part + 1, hi)


nums = [2,8,7,1,3,5,6,4]
qucikSort(nums, 0, len(nums) - 1)

print(nums)

# 틀렸음