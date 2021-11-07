#92

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right - left == 0:
            return head

        left_space = None
        rev = None
        right_space = None
        count = 1
        while head != None:
            if count < left:
                left_space, left_space.next, head = head, left_space, head.next
            elif count > right:
                right_space, right_space.next, head = head, right_space, head.next
            else:
                rev, rev.next, head = head, rev, head.next
            count += 1

        rev_rev = None
        while rev != None:
            rev_rev, rev_rev.next, rev = rev, rev_rev, rev.next

        result = None
        while right_space != None:
            result, result.next, right_space = right_space, result, right_space.next
        while rev_rev != None:
            result, result.next, rev_rev = rev_rev, result, rev_rev.next
        while left_space != None:
            result, result.next, left_space = left_space, result, left_space.next

        return result