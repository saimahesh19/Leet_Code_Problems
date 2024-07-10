class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = sorted(set(nums))
        for i in range(len(unique_nums)):
            nums[i] = unique_nums[i]
        return len(unique_nums)
