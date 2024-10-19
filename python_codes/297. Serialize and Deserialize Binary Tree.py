class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        def dfs(node):
            if not node:
                return "None,"
            return str(node.val) + "," + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        def dfs(nodes):
            val = nodes.pop(0)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = dfs(nodes)
            node.right = dfs(nodes)
            return node
        
        node_list = data.split(",")
        return dfs(node_list)
