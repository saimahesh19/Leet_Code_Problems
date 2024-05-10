class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1
