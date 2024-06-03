class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        def delete_node(root, key):
            if root is None:
                return root
            if key < root.val:
                root.left = delete_node(root.left, key)
            elif key > root.val:
                root.right = delete_node(root.right, key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                temp = find_min(root.right)
                root.val = temp.val
                root.right = delete_node(root.right, temp.val)
            return root
        def find_min(node):
            current = node
            while current.left is not None:
                current = current.left
            return current
        root = delete_node(root, key)
        return root
