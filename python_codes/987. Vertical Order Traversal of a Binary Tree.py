# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode):
        
        node_list = []

        
        def dfs(node, row, col):
            if node:
                
                node_list.append((col, row, node.val))
                
                dfs(node.left, row + 1, col - 1)
                
                dfs(node.right, row + 1, col + 1)

        
        dfs(root, 0, 0)

        
        def sort_key(node):
            col, row, value = node
            return (col, row, value)

       
        node_list.sort(key=sort_key)

        
        result = defaultdict(list)

        
        for col, row, value in node_list:
            result[col].append(value)

        
        return [result[x] for x in sorted(result)]
        
