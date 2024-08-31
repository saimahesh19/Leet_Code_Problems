class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if nums == sorted(nums, reverse=True):
            nums[:] = nums[::-1]
        else:
            x = nums[::-1]
            for i in range(n - 1):
                if x[i] > x[i + 1]:  
                    for j in range(i + 1):
                        if x[j] > x[i + 1]: 
                            x[j], x[i + 1] = x[i + 1], x[j]
                            break
                    break
            nums[:] = x[::-1][:n - i - 1] + sorted(x[::-1][n - i - 1:])
