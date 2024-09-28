from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        # Variables to check if the first row and first column need to be zero
        first_row_zero = False
        first_col_zero = False
        
        # Determine if the first row has any zeroes
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # Determine if the first column has any zeroes
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        # Use the first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark this row to be zeroed
                    matrix[0][j] = 0  # Mark this column to be zeroed
        
        # Zero out cells based on the markers in the first row and first column
        for i in range(1, m):
            if matrix[i][0] == 0:  # If this row should be zeroed
                for j in range(1, n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:  # If this column should be zeroed
                for i in range(1, m):
                    matrix[i][j] = 0
        
        # Finally, zero out the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Finally, zero out the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
