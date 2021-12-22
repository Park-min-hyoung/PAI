#226

# 우아한 풀이
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None

# 반복구조 BFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([])

        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

# 반복구조 DFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])

        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left

            self.invertTree(node.left)
            self.invertTree(node.right)

        return root

# 반복구조 DFS 후위 순위
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])

        node = stack.pop()
        if node:
            self.invertTree(node.left)
            self.invertTree(node.right)

            node.left, node.right = node.right, node.left

        return root