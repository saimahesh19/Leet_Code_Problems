# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        res = []
        
        def dfs(node):
            if node is None:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)  # Start the DFS traversal
        unique_values = sorted(set(res))  # Get unique values and sort them
        
        if len(unique_values) < 2:
            return -1  # No second minimum exists
        return unique_values[1]  # Return the second minimum
