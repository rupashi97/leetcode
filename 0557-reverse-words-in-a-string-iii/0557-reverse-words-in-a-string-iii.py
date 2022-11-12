class Solution:
    def reverseWords(self, s: str) -> str:

        revs = " ".join(word[::-1] for word in s.split())
        
        return revs
        
            
        