class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []
        def dfs(node, l):
            if node is None:
                return
            if node.left is None and node.right is None:
                l.append(node.val)
                return
            dfs(node.left, l)
            dfs(node.right, l)
        dfs(root1, l1)
        dfs(root2, l2)
        return l1 == l2
