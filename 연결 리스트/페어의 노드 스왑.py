#24

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        rev = None
        cnt = 0
        while head != None:
            rev, rev.next, head = head, rev, head.next
            cnt += 1

        result = None
        while rev != None:
            if cnt % 2 != 0:
                result, result.next, rev = rev, result, rev.next
                cnt += 1

            result, result.next.next, rev = rev, result, rev.next.next

        return result