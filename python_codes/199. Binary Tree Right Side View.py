class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        def dfs(node, level):
            if node:
                if level == len(res):
                    res.append(node.val)
                dfs(node.right, level + 1)
                dfs(node.left, level + 1)
        dfs(root, 0)
        return res
