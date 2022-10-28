class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        
        row, col = len(mat), len(mat[0])
        
        # up pass
        
        dup = [(0, -1), (-1,0)]
        
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0: continue

                up = float('inf') if i<=0 else mat[i-1][j]
                left = float('inf') if j<=0 else mat[i][j-1]
                    
                mat[i][j] = min(left, up) + 1 # check valid
                
                
        for i in reversed(range(row)):
            for j in reversed(range(col)):
                if mat[i][j]==0: continue
                
                right = float('inf') if j+1>=col else mat[i][j+1]
                bel = float('inf') if i+1>=row else mat[i+1][j]
                mat[i][j] = min(mat[i][j], bel+1, right+1)
                
                
        return mat