
'''
Use hash table [dictionary in python] logic as lookup complexity in hash table ~ O(1).
Overall code complexity : O(n) with one pass
'''

class Solution:

    def twoSum(self, nums: list, target: int) -> list:
        hashmap = {}
        for i in range(len(nums)):
            res = target - nums[i]

            if res in hashmap:
                return [i, hashmap[res]]

            hashmap[nums[i]] = i
