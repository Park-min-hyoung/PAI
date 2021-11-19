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