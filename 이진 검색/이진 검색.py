# 704
def binary(left, right):
    if left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            binary(left, mid - 1, result)
        else:
            binary(mid + 1, right, result)

    return -1

nums = [5]
target = 5

print(binary(0, len(nums) - 1))