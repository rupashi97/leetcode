class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
           
        r, c = len(mat), len(mat[0])
        dist =  [[0]*c]*r
        
        # from top to bottom - 1st pass
        for i in range(r):
            for j in range(c):         
                if mat[i][j] :
                    top = mat[i-1][j] if i > 0 else math.inf
                    left = mat[i][j-1] if j > 0 else math.inf
                    mat[i][j] = min(top, left)+1
        
        # from bottom to top - 2nd pass
        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                
                if mat[i][j] :
                    bottom = mat[i+1][j] if i < r-1 else math.inf
                    right = mat[i][j+1] if j < c-1 else math.inf
                    
                    mat[i][j] = min(mat[i][j], bottom + 1, right + 1)
                       
        
        return mat
        
            