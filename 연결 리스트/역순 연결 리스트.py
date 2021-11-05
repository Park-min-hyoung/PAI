# 206

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None

        while head != None:
            rev, rev.next, head = head, rev, head.next

        return rev