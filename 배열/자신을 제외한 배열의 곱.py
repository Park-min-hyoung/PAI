#238
nums = [1, 2, 3, 4]

out = []
p = 1
for i in range(len(nums)):
    out.append(p)
    p *= nums[i]

p = 1
for i in range(len(nums) - 1, -1, -1):
    out[i] *= p
    p *= nums[i]

print(out)

# 틀렸음
'''
1. 자기 자신을 제외한 왼쪽 곱셈 리스트와 오른쪽 곱셈 리스트를 만든 후 두 배열의 동일한 index끼리 곱해주면 된다.'''