class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_elements = sum(nums)
        F_k = sum(i * nums[i] for i in range(n))
        maxi = F_k
        for i in range(1, n):
            F_k = F_k + sum_of_elements - n * nums[-i]
            maxi = max(maxi, F_k)
        return maxi
