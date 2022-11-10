import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        
        if m*n != (r*c):
            return mat
        
        return np.reshape(mat, (r, c))
#         for i in range(m):
#             for j in range(n):
                