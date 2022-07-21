from typing import List


# Very efficient | Discussions solutions
def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = set()

    # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)

    # 2. Create a separate set for negatives and positives for O(1) look-up times
    N, P = set(n), set(p)

    # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
    #   i.e. (-3, 0, 3) = 0
    if z:
        for num in P:
            if -1 * num in N:
                res.add((-1 * num, 0, num))

    # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
    if len(z) >= 3:
        res.add((0, 0, 0))

    # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
    #   exists in the positive number set
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            target = -1 * (n[i] + n[j])
            if target in P:
                res.add(tuple(sorted([n[i], n[j], target])))

    # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
    #   exists in the negative number set
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            target = -1 * (p[i] + p[j])
            if target in N:
                res.add(tuple(sorted([p[i], p[j], target])))

    return res

# Efficient | O(n^2) -- Preferred
def threeSum(self, nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return res

# My solution | V Bad result = 6%
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res, triplet = [], []
        lookup, uniq = {}, {}

        for i, n in enumerate(nums):
            lookup[n] = i

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if -(nums[i] + nums[j]) in lookup:
                    x = lookup[-(nums[i] + nums[j])]
                    if x != i and x != j:
                        triplet = [nums[i], nums[j], -(nums[i] + nums[j])]
                        triplet.sort()

                        if str(triplet) not in uniq:
                            uniq[str(triplet)] = 1
                            res.append(triplet)

        return res
