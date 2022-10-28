from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        
        queue = deque([(sr,sc)])
        
        startCol = image[sr][sc]
        row, col = len(image), len(image[0])
        
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        
        if startCol == color: return image
        
        while queue:
            
            r,c = queue.popleft()
            # r, c = pos[0], pos[1]
            image[r][c] = color
            
            for d in dirs:
                newr, newc = r + d[0], c + d[1]
                
                if 0<=newr<row and 0<=newc<col and image[newr][newc]==startCol:
                    image[newr][newc]=color
                    queue.append((newr,newc))
                    
                    
        return image
        