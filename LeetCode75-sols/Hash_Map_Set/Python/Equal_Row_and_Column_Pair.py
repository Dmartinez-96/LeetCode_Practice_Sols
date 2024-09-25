class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_counts = {}
        col_counts = {}

        for i in range(n):
            row = tuple(grid[i])
            if row in row_counts:
                row_counts[row] += 1
            else:
                row_counts[row] = 1
        for i in range(n):
            col = []
            for j in range(n):
                col.append(grid[j][i])
            col = tuple(col)
            if col in col_counts:
                col_counts[col] += 1
            else:
                col_counts[col] = 1
        
        total_pairs = 0
        for row in row_counts:
            if row in col_counts:
                total_pairs += row_counts[row] * col_counts[row]
        return total_pairs
