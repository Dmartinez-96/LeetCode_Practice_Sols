from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Directions for all 8 neighbors (horizontal, vertical, diagonal)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        
        m, n = len(board), len(board[0])
        
        # Helper function to count live neighbors
        def count_live_neighbors(row, col):
            live_neighbors = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and abs(board[r][c]) == 1:
                    live_neighbors += 1
            return live_neighbors
        
        # Step 1: Apply rules and use intermediate states
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                
                # Rule 1 or 3: Any live cell with fewer than 2 or more than 3 live neighbors dies.
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1  # Mark as a live cell that will die.
                
                # Rule 4: Any dead cell with exactly 3 live neighbors becomes a live cell.
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2  # Mark as a dead cell that will become live.
        
        # Step 2: Final pass to clean up the board
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0  # Live cell has died
                elif board[i][j] == 2:
                    board[i][j] = 1  # Dead cell has become live
