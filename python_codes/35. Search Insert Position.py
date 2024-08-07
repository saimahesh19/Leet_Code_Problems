class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        
        def fun(l, r):
            if l > r:
                return l 
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return fun(mid + 1, r)
            else:
                return fun(l, mid - 1)
        
        return fun(l, r)
