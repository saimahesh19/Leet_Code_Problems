class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirstPosition(nums, target):
            left, right = 0, len(nums) - 1
            position = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    position = mid
                    right = mid - 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return position

        def findLastPosition(nums, target):
            left, right = 0, len(nums) - 1
            position = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    position = mid
                    left = mid + 1 
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return position

        firstPosition = findFirstPosition(nums, target)
        lastPosition = findLastPosition(nums, target)
        
        return [firstPosition, lastPosition]
