class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        temp2 = [[] for _ in range(n)]
        
        for i in range(n):
            temp1 = []
            for j in range(n):
                temp1.append(matrix[j][i])
            temp1.reverse()
            temp2[i] = temp1
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp2[i][j]
