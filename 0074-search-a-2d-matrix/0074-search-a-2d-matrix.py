class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        arr = []
        arr = [val for row in matrix for val in row]
        print(arr)
        
        b, l = 0, m*n - 1
        while b<=l:
            mid = (b+l)//2
            if target == arr[mid]: return True
            if target>arr[mid]: 
                b=mid+1
            else: l=mid-1
                
        return False
            