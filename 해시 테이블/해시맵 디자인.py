class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)

        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next

        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size

        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next

        return -1

    def remove(self, key: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            return

        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

# 틀렸음
'''
1. put은 해당 index에 연결리스트가 없을때와 있을때로 구분, 있을경우에 새로운 key와 기존 key가 일치하는 경우 업데이트
없으면 연결리스트 마지막에 추가
2. get은 해당 index에 연결리스트가 없을때와 있을 때(put과 비슷하다)
3. remove는 해당 index에 연결리스트가 없을때와 있을 때, 있을 경우 2가지로 나누어 질 수 있다
4. 첫 번째 경우 삭제하려는 key가 연결리스트의 첫번째 key와 동일한 경우에서 연결리스트에 이 노드 한개 밖에 없을 경우
그냥 빈 연결리스트로 초기화 시켜주면 되고 그것이 아닐경우 다음 연결리스트로 초기화 시킨다
5. 두 번째 경우는 삭제하려는 key가 연결리스트의 두 번째 key 부터 있을 경우로서 하나씩 순회하면서 삭제하려는 key가 연결리스트에
있다면 삭제하고 없다면 그냥 끝난다.'''