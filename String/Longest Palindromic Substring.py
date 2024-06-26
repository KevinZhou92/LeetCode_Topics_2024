"""
Solution 1:

Start from cur char, it could either be the center of the palindrome or 
could become center with the element to the left

Time Complexity: O(N^2)
Space complexity : O(1)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        
        res = ""
        for index in range(len(s)):
            p1 = self.findPalindrome(s, index, index)
            p2 = self.findPalindrome(s, index, index + 1)
            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2
        
        return res
    
    def findPalindrome(self, s, l, r):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                return s[l + 1:r]
  
        return s[l + 1:r]
