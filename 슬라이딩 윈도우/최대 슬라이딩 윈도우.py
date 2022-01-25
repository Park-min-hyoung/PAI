#239

from collections import deque

nums = [1,3,-1,-3,5,3,6,7]
k = 3

result = []
queue = deque()
for idx, num in enumerate(nums):
    while queue and nums[queue[-1]] <= num:
        queue.pop()

    queue.append(idx)

    if idx - queue[0] >= k:
        queue.popleft()

    if idx + 1 >= k:
        result.append(nums[queue[0]])

print(result)

# 틀렸음
'''
1. nums의 index를 하나씩 추가하면서 max 값을 result에 append 하는 작업을 시작(지나온 index 길이가 k(슬라이딩 길이)보다 크거나 같을때)
2. queue에 현재 index에 해당하는 값 보다 작은 값이 없을때 까지 이전 값들을 제거해준다. => 이 작업을 하게 되면 nums[queue[0]]이 최대값이 된다.
3. 현재 index와 가장 먼저 queue에 들어온 index 간의 길이가 허용 길이(k)를 넘어서면 가장 먼저 들어온 index를 제거'''