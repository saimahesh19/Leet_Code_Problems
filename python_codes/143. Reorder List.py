class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        n = len(nodes)
        i, j = 0, n - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i < j:
                nodes[j].next = nodes[i]
                j -= 1
        
        nodes[i].next = None  

        return
