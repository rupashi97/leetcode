class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        row, col = len(grid), len(grid[0])
        queue = []
        freshOrange = 0
        minutes = -1
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append((i,j))
                    
                elif grid[i][j]==1:
                    freshOrange += 1
                    
        queue.append((-1,-1))  # to mark the end of the level
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while queue:
            pos = queue.pop(0)
            x, y = pos[0], pos[1]
            if x == -1:
                minutes += 1
                if queue:
                    queue.append((-1,-1))
            
            else:
                for d in directions:
                    r, c = x + d[0], y + d[1]
                    if r<0 or r>=row or c<0 or c>=col: continue

                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        freshOrange -= 1
                        queue.append((r,c))
                
                
        return minutes if freshOrange == 0 else -1
            
            
            
            
        
        