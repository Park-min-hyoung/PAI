# 206

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None

        while head:
            rev, rev.next, head = head, rev, head.next

        return rev

# 재귀 구조로 뒤집기
'''class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev

            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)'''