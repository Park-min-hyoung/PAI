#2

# 전가산기 구현
'''class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(None)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next'''

# 자료형 변환 이용
'''class Solution:
    # 연결 리스트를 반대로
    def reverseList(self, head):
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next

        return rev

    # 연결 리스트를 파이썬의 리스트로
    def toList(self, node):
        list = []
        while node:
            list.append(node.val)
            node = node.next

        return list

    # 파이썬 리스트(더해진 값)를 연결 리스트로
    def toReversedLinkedList(self, result):
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return prev

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(map(str, a))) + int(''.join(map(str, b)))

        return self.toReversedLinkedList(str(resultStr))'''

# 틀렸음(v)
'''
1. 함수 여러개(연결 리스트 뒤집기, 연결 리스트를 파이썬 리스트로, 더해진 값을 연결리스트로)를 사용해서 값을 구하는 방법
2. 전가산기 구현 방법 사용해서 몫과 나머지를 통해 연결리스트에 하나씩 삽입하는 방법'''