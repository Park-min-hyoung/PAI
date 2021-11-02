#1
nums = [2,7,14,9]
target = 9

result = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if target == nums[i] + nums[j]:
            result.append([i, j])

f_result = ' '.join(map(str, result))

print(f_result)