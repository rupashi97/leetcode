'''

Given to binary numbers (in str format); add to get result in binary
'''
# Fastest 38ms
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        anum, bnum = 0, 0

        for i in range(len(a)):
            anum += int(a[-i - 1]) * (2 ** i)

        for i in range(len(b)):
            bnum += int(b[-i - 1]) * (2 ** i)

        cnum = anum + bnum
        cstr = ""

        if cnum <= 1: return str(cnum)

        while cnum > 1:
            cstr += str(cnum % 2)
            cnum = cnum // 2

        cstr += str(cnum)
        return cstr[::-1]


class Solution2:
    def addBinary(self, a: str, b: str) -> str:

        anum, bnum = 0, 0

        for i in range(len(a)):
            anum += int(a[-i - 1]) * (2 ** i)

        for i in range(len(b)):
            bnum += int(b[-i - 1]) * (2 ** i)

        return bin(anum+bnum).replace("0b", "")


class Solution3:
    def addBinary(self, a: str, b: str) -> str:
        anum = int(a, 2)
        bnum = int(b, 2)
        return bin(anum + bnum).replace("0b", "")



