import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        if (m*n) != (r*c): return mat
        
        res, temp = [], []
        
        for i in range(m):
            for j in range(n):
                temp.append(mat[i][j])
                if (len(temp) != c): continue  
                res.append(temp)
                temp = []    
        
        return res