class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if target>matrix[i][n-1]: continue
            for j in range(n):
                if target==matrix[i][j]: return True
            
            return False