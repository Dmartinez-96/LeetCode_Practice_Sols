from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create sets for each row, column, and sub-box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Iterate through each cell in the board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                
                # Calculate the index of the corresponding 3x3 sub-box
                box_index = (i // 3) * 3 + (j // 3)
                
                # Check for duplicates in the row, column, and sub-box
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False
                
                # Add the number to the respective row, column, and sub-box sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
        
        # If no conflicts are found, the board is valid
        return True
