#1
nums = [2,7,11,15]
target = 9

# 조회 구조 개선
'''dict_map = {}
for i, num in enumerate(nums):
    if target - num in dict_map:
        return [i, dict_map[target - num]]
    dict_map[num] = i'''

# 첫 번째 수를 뺀 결과 키 조회(집합사용)(틀렸음)
# key와 value를 뒤집음으로써 index를 value로 사용(어차피 출력결과는 index 번호이므로...)
'''dict_map = {}
for i, value in enumerate(nums):
    dict_map[value] = i

for i, value in enumerate(nums):
    if target - value in dict_map and i != dict_map[target - value]:
        return [i, dict_map[target - value]]'''

#in 사용(틀렸음)
'''for i, n in enumerate(nums):
    comp = target - n

    if comp in nums[i + 1:]:
        print([nums.index(n), nums[i + 1:].index(comp) + (i + 1)])'''

#브루트 포스로 계산
'''result = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if target == nums[i] + nums[j]:
            result.append([i, j])

f_result = ' '.join(map(str, result))

print(f_result)'''