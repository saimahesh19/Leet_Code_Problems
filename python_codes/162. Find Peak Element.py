class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxi = nums[0]
        n = len(nums)
        pos = 0
        for i in range(1, n):
            if maxi < nums[i]:
                maxi = nums[i]
                pos = i
        return pos
