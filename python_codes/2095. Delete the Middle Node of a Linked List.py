class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
        current_node = head
        while current_node:
            node_list.append(current_node.val)
            current_node = current_node.next
        length = len(node_list)
        middle_index = length // 2
        node_list.pop(middle_index)
        new_head = ListNode(None)
        current_node = new_head
        for val in node_list:
            current_node.next = ListNode(val)
            current_node = current_node.next
        return new_head.next

        
