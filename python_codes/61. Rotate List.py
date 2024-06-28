class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        h = []
        current = head
        while current:
            h.append(current.val)
            current = current.next
        
        n = len(h)
        k = k % n  # To handle cases where k > n
        
        if k == 0:
            return head
        
        a = h[-k:] + h[:-k]
        
        dummy = ListNode(0)
        current = dummy
        for val in a:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next
