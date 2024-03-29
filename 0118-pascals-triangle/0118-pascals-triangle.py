class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows==1: return [[1]]

        elif numRows==2: return [[1],[1,1]]
        
        res = [[1],[1,1]]
        
        for i in range(2, numRows):   
            temp = [ res[i-1][j] + res[i-1][j+1]  for j in range(i-1)]
            res.append([1] + temp + [1])   
            
        return res 
