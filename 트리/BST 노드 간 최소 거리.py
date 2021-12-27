#783

# 재귀 구조로 중위 순회
class Solution:
    result = sys.maxsize
    prev = -sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result

# 반복 구조로 중위 순회
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result = sys.maxsize
        prev = -sys.maxsize

        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result