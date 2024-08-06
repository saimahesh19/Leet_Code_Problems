class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        def subarraysum(nums):
            sas = []
            for i in range(len(nums)):
                ws = 0
                while i + ws < len(nums):
                    sas.append(sum(nums[i:i+ws+1]))
                    ws += 1
            sas.sort()
            return sas
        
        sas = subarraysum(nums)
        return sum(sas[left-1:right])% (10**9 + 7)
