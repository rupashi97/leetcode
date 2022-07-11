'''
Find out if a phrase is a palindrome
after
Converting all upper case to lower
Removing all non-alpha numeric characters
'''

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # sarr = list(filter(str.isalnum, s.lower()))
        # s = ''.join(e for e in s if e.isalnum()).lower()

        sarr = list(re.sub('[^a-zA-Z0-9]', '', s.lower()))

        # return sarr == sarr[::-1]

        for i in range(int(len(sarr) / 2)):
            if sarr[i] != sarr[-i - 1]:
                return False
        return True




