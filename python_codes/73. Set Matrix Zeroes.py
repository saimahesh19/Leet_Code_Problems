class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rowzero(p):
            for i in range(len(matrix[0])):
                matrix[p][i] = 0
        def colzero(p):
            for i in range(len(matrix)):
                matrix[i][p] = 0
        rows, cols = len(matrix), len(matrix[0])
        zero_positions = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))
        for r, c in zero_positions:
            rowzero(r)
            colzero(c)
