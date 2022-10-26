class Solution:
    
    def explore(self, grid, r, c, visited):
        
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]): return False
        
        if grid[r][c]=="0": return False
        if (r,c) in visited: return False
            
        visited.add((r,c))
        
        self.explore(grid, r-1, c, visited)
        self.explore(grid, r+1, c, visited)
        self.explore(grid, r, c-1, visited)
        self.explore(grid, r, c+1, visited)
        
        
        return True
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row, col = len(grid), len(grid[0])
        
        visited = set()
        count = 0
        for i in range(row):
            for j in range(col):
                if self.explore(grid, i, j, visited):
                    count +=1
                    
        return count
                
    
    
        