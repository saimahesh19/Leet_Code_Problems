class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        
        # Move all non-zero elements to the beginning of the list
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        
        # Fill the rest of the list with zeros
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0
