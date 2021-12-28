#105

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            idx = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[idx])
            node.left = self.buildTree(preorder, inorder[:idx])
            node.right = self.buildTree(preorder, inorder[idx + 1:])

            return node