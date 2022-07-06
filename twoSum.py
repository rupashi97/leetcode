
class Solution:

    def twoSum(self, nums: list, target: int) -> list:
        hashmap = {}
        for i in range(len(nums)):
            res = target - nums[i]

            if res in hashmap:
                return [i, hashmap[res]]

            hashmap[nums[i]] = i
