class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums = []  
        for i in range(numRows):
            nums.append([0] * (i + 1))
            nums[i][0], nums[i][i] = 1, 1 
            for j in range(1, i):
                nums[i][j] = nums[i-1][j-1] + nums[i-1][j]
        return nums
