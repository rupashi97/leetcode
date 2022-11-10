class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        if (m*n) != (r*c): return mat
        
        queue = [ val for row in mat for val in row ]
        
        res = [ queue[i:c+i] for i in range(0, r*c, c) ]
        return res
