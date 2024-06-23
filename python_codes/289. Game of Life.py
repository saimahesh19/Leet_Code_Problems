class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def get_live_neighbors(matrix, row, col):
            live_neighbors = 0
            m = len(matrix)
            n = len(matrix[0])
            directions = [
                (1, 0), (-1, 0), (0, 1), (0, -1),  # Up, down, right, left
                (1, 1), (-1, 1), (1, -1), (-1, -1)  # Diagonals
            ]
            for (dr, dc) in directions:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < m and 0 <= new_col < n and matrix[new_row][new_col] in (1, 2):
                    live_neighbors += 1
            return live_neighbors
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                live_neighbors = get_live_neighbors(board, i, j)
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # Mark for death
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = 3  # Mark for birth
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0  # Dead
                elif board[i][j] == 3:
                    board[i][j] = 1  # Alive
