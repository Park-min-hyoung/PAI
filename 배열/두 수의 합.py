#1
nums = [2,7,11,15]
target = 9

# 첫 번째 수를 뺀 결과 키 조회(집합사용)(틀렸음)
# key와 value를 뒤집음으로써 index를 value로 사용(어차피 출력결과는 index 번호이므로...)
# 여기 책 개념부터 훑어 보기
'''dict = {}
for i, num in enumerate(nums):
    dict[num] = i

for i, num in enumerate(nums):
    if target - num in dict and i != dict[target - num]:
        print([i, dict[target - num]])
        exit()'''

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