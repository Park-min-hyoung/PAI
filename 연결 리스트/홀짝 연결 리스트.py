# 328

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        even = even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        print(head)

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = None
        even = None
        while head != None:
            odd, odd.next, head = head, odd, head.next
            if head == None:
                break
            even, even.next, head = head, even, head.next

        result = None
        while even != None:
            result, result.next, even = even, result, even.next
        while odd != None:
            result, result.next, odd = odd, result, odd.next

        return result
