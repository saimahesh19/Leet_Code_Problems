
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        a = matrix
        flag = False
        for i in range(m):
            if a[i][0] <= target <= a[i][n - 1]:
                if target in a[i]:
                    flag = True
        return flag
