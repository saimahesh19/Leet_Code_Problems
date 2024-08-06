class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct_elements = [i for i in arr if arr.count(i) == 1]
        
        if k <= len(distinct_elements):
            return distinct_elements[k-1]
        else:
            return ""
