#561
nums = [6,2,6,5,1,2]
nums.sort()
max_sum = 0

for i in range(0, len(nums), 2):
    max_sum += nums[i]

print(max_sum)