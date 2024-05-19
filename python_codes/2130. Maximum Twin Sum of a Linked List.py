class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        list_node = []
        current_node = head
        while current_node:
            list_node.append(current_node.val)
            current_node = current_node.next
        n = len(list_node)
        max_sum = 0
        for i in range(n // 2):
            pair_sum = list_node[i] + list_node[n - i - 1]
            if pair_sum > max_sum:
                max_sum = pair_sum
        return max_sum
