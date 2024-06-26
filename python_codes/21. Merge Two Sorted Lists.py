# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a1 = []
        a2 = []
        while list1:
            a1.append(list1.val)
            list1 = list1.next 
        while list2:
            a2.append(list2.val)
            list2 = list2.next  
        i = 0
        j = 0
        res = []
        while i < len(a1) and j < len(a2):  
            if a1[i] >= a2[j]:
                res.append(a2[j])
                j += 1
            else:
                res.append(a1[i])
                i += 1
        if i < len(a1):  
            while i < len(a1):
                res.append(a1[i])
                i += 1
        else:
            while j < len(a2):  
                res.append(a2[j])
                j += 1
        r = ListNode(0)
        current = r  
        k = 0
        while k < len(res): 
            current.next = ListNode(res[k])
            current = current.next  
            k += 1
        return r.next  
