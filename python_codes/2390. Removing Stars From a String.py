class Solution:
    def removeStars(self, s: str) -> str:
        lists = list(s)
        i = j = 0
        while i < len(lists):
            if lists[i] == "*":
                if j > 0 and lists[j - 1] != "*": 
                    j -= 1  
                i += 1  
            else:
                lists[j] = lists[i]  
                i += 1
                j += 1
        return ''.join(lists[:j]) 
