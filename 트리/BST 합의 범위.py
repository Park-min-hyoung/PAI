#938

# DFS 가지치기로 필요한 노드 탐색
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0

            if node:
                if node.val < low:
                    return dfs(node.right)
                elif node.val > high:
                    return dfs(node.left)
                return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)

# 반복 구조로 DFS로 필요한 노드 탐색
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, sum = [root], 0
        while stack:
            node = stack.pop()

            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val

        return sum

# BFS 이용
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue, sum = collections.deque([root]), 0
        while queue:
            node = queue.popleft()

            if node:
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
                if low <= node.val <= high:
                    sum += node.val

        return sum