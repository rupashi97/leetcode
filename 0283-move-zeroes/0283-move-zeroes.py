class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for _ in range(len(nums)):
            x = nums[i]
            if x==0:
                nums.pop(i)
                nums.append(x)
            else:
                i +=1
                
        