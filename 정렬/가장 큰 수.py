#179

nums = [34323,3432]
nums_str = list(str(x) for x in nums)
nums_str.sort(reverse=True)
print(nums_str)

for i in range(len(nums_str) - 1, 0, -1):
    if nums_str[i][-1] >= nums_str[i - 1][-1]:
        nums_str[i], nums_str[i - 1] = nums_str[i - 1], nums_str[i]

print(''.join(nums_str))

# 틀렸음