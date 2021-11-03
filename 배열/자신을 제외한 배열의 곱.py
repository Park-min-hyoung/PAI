#238
nums = [0, 4, 0]

all_value = 1
zero_count = 0
for num in nums:
    if num == 0:
        zero_count += 1
        continue
    all_value *= num

# 원소가 모두 0일때
if len(nums) == zero_count:
    print(nums)
    exit()

result = []
for num in nums:
    if zero_count == 0:
        result.append(all_value // num)
    else:
        if num != 0:
            result.append(0)
        else:
            if zero_count == 1:
                result.append(all_value)
            else:
                result.append(0)

print(result)