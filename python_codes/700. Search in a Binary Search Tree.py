class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def find(root, val):
            if not root:
                return None
            if root.val == val:
                return root
            elif root.val < val:
                return find(root.right, val)
            else:
                return find(root.left, val)
        return find(root, val)
