class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s = {}
        for i in nums:
            if i in s:
                s[i] += 1
            else:
                s[i] = 1
        
        l = len(nums) // 3
        res = []
        for j, k in s.items():
            if k > l:
                res.append(j)
        
        return res
