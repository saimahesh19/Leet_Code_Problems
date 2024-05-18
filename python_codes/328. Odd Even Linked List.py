class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
        new_list = []
        current_node = head
        while current_node:
            node_list.append(current_node.val)
            current_node = current_node.next
        for i in range(len(node_list)):
            if i % 2 == 0:
                new_list.append(node_list[i])
        for i in range(len(node_list)):
            if i % 2 != 0:
                new_list.append(node_list[i])
        new_head = ListNode(None)
        current_node = new_head
        for val in new_list:
            current_node.next = ListNode(val)
            current_node = current_node.next
        return new_head.next
