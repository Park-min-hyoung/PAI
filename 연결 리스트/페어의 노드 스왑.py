#24

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 반복 구조로 스왑
'''class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next

        return root.next'''

# 값만 교환
'''class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next

        return cur'''

# 틀렸음
'''
1. 순수하게 값만 교환하는 변칙적인 방법도 있음
2. 두 번째 방법은 값만 교환하는 것이 아니라 연결 리스트 자체를 바꾸는 방법도 있다
(앞 뒤 노드를 바꾸는 작업도 해주어야 하며 바뀐 두 노드 옆에 노드 들도 정상적으로 연결 될 수 있도록 작업을 해줘야 한다)'''