class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res, triplet = [], []
        lookup, uniq = {}, {}

        for i, n in enumerate(nums):
            lookup[n]=i
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if -(nums[i]+nums[j]) in lookup:
                    x = lookup[-(nums[i]+nums[j])]
                    if x!=i and x!=j:
                        triplet = [nums[i], nums[j], -(nums[i]+nums[j])] 
                        triplet.sort()
                        
                        if str(triplet) not in uniq:
                            uniq[str(triplet)]=1
                            res.append(triplet)
                            

                         
        return res
            
            
               