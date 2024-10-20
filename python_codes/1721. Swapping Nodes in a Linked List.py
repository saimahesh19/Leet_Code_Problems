# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0
        if head is None:
            return None
        
        current = head
        while current:
            l += 1
            current = current.next
        
        if k > l:
            return None
        
        head1 = head
        for i in range(0, k - 1):
            head1 = head1.next
        
        head2 = head
        for i in range(0, l - k):
            head2 = head2.next
        
        # Swap the values of head1 and head2 instead of the nodes
        head1.val, head2.val = head2.val, head1.val
        
        return head
