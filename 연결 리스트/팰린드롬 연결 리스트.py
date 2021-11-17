#234

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#런너를 이용한 우아한 풀이
'''class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next

            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next

        return not rev'''

# 데크를 이용한 최적화
'''class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = deque()

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True'''

# 리스트 변환
'''class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True'''

# 틀렸음(v)
'''
1. slow와 fast를 이용한 런너 기법'''