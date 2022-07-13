'''
Find first bad version of software

[1 2 3 4 ...... n]
[g g g g g b b]   -> Ans = 6

Fancy Binary Search Algorithm
'''


# The isBadVersion API is already defined for you = Hidden function/ API for use
def isBadVersion(version: int) -> bool:
    return True  # Can return anything


class Solution:
    def firstBadVersion(self, n: int) -> int:

        b, l = 1, n
        res = 1

        while b <= l:
            m = int((b + l) / 2)   # can also be written as  (b+1) // 2

            if isBadVersion(m):
                res = m
                l = m - 1
            else:
                b = m + 1

        return res
