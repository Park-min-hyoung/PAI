# 23

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for list in lists:
            while list:
                heapq.heappush(heap, list.val)
                list = list.next

        root = head = ListNode(None)

        while heap:
            head.next = ListNode(heapq.heappop(heap))
            head = head.next

        return root.next

# 우선순위 큐를 이용한 리스트 병합
'''import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next'''