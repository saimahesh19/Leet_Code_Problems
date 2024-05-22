class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0
        def dfs(node, direction, length):
            if not node:
                return
            self.maxLength = max(self.maxLength, length)
            if direction == 'left':
                if node.left:
                    dfs(node.left, 'right', length + 1)
                if node.right:
                    dfs(node.right, 'left', 1)
            elif direction == 'right':
                if node.right:
                    dfs(node.right, 'left', length + 1)
                if node.left:
                    dfs(node.left, 'right', 1) 
        if root:
            if root.left:
                dfs(root.left, 'right', 1)
            if root.right:
                dfs(root.right, 'left', 1)    
        return self.maxLength
