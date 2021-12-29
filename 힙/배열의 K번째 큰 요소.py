#215

# heapq 모듈 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in nums:
            heapq.heappush(heap, -i)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return -heap[0]

# heapq 모듈의 nlargest 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

# heapq 모듈의 heapify 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return nums[0]

# 정렬을 이용한 풀이
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]