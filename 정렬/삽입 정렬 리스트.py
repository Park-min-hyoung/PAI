#147

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        lst = []

        while p:
            lst.append(p.val)
            p = p.next

        for i in range(1, len(lst)):
            idx = i
            value = lst[idx]

            for j in range(idx - 1, -1, -1):
                if value >= lst[j]:
                    break
                idx -= 1
                lst[j + 1] = lst[j]
            lst[idx] = value

        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head