"""
Solution 1:

Two pointer

Be careful about conditions

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and (not s[l].isalpha() and not s[l].isnumeric()):
                l += 1
            while l < r and (not s[r].isalpha() and not s[r].isnumeric()):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True
