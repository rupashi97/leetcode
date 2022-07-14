'''

'''

import math


class Solution:
    def climbStairs(self, n: int) -> int:
        sum = 1
        for y in range(1, (n // 2) + 1):
            sum += math.factorial(n - y) / (math.factorial(y) * math.factorial(n - 2 * y))

        return int(sum)
