class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums: List[int], target: int, left: int, right: int) -> int:
            if left > right:
                return -1 

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:  
                if nums[left] <= target < nums[mid]:  
                    return binary_search(nums, target, left, mid - 1)
                else:  
                    return binary_search(nums, target, mid + 1, right)
            else:  
                if nums[mid] < target <= nums[right]: 
                    return binary_search(nums, target, mid + 1, right)
                else: 
                    return binary_search(nums, target, left, mid - 1)

        return binary_search(nums, target, 0, len(nums) - 1)
