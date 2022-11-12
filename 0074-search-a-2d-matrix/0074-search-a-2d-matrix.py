class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        res = set([val for row in matrix for val in row])
        
        if target in res: return True
        return False
        
        