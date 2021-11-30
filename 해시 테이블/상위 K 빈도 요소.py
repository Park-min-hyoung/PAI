# 347

from collections import Counter
import collections
import heapq

nums = [1,1,1,2,2,3]
k = 2
result = []

# 파이썬다운 방식
'''print(list(zip(*Counter(nums).most_common(k)))[0])'''

# Counter를 이용한 음수 순 추출
'''nums_dict = Counter(nums)
heap = []
for dic in nums_dict:
    heapq.heappush(heap, (-nums_dict[dic], dic))

for _ in range(k):
    result.append(heapq.heappop(heap)[1])'''

# 내 풀이
'''nums_dict = collections.defaultdict(int)
for num in nums:
    nums_dict[num] += 1
nums_dict = sorted(nums_dict.items(), key=lambda x: (-x[1]))

for i in range(k):
    result.append(nums_dict[i][0])'''

print(result)