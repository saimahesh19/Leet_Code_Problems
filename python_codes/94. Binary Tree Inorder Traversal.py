class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorderTraversal(root):
            result = []
            inorderHelper(root, result)
            return result

        def inorderHelper(node, result):
            if node:
                inorderHelper(node.left, result)
                result.append(node.val)
                inorderHelper(node.right, result)
        
