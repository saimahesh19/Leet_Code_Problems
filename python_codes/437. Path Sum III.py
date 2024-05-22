class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, currentSum):
            if not node:
                return
            currentSum += node.val
            if currentSum == targetSum:
                self.count += 1
            dfs(node.left, currentSum)
            dfs(node.right, currentSum)
        def findPaths(node):
            if not node:
                return
            dfs(node, 0)
            findPaths(node.left)
            findPaths(node.right)
        self.count = 0
        findPaths(root)
        return self.count
