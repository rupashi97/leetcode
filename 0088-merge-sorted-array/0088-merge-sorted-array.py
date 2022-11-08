class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i, j, k = 0, 0, 0
        nums3 = [0]*(m+n)
        
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                nums3[k] = nums1[i]
                i+=1
            else:
                nums3[k] = nums2[j]
                j+=1
            k+=1
        
        for x in range(i,m):
            nums3[k] = nums1[x]
            k+=1
            
        for x in range(j,n):
            nums3[k] = nums2[x]
            k+=1
            
        for i in range(len(nums3)):
            nums1[i]=nums3[i]
        