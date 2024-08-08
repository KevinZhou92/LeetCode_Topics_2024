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
                return s[l + 1 : r]

        return s[l + 1 : r]


"""
Solution 2:

Check from center, return index instead of substring each check

Time Complexity: O(N^2)
Space complexity : O(1)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0

        res = [0, 0]
        for index in range(len(s)):
            p1 = self.findPalindrome(s, index, index)
            p2 = self.findPalindrome(s, index, index + 1)
            if p1[1] - p1[0] > res[1] - res[0]:
                res = p1
            if p2[1] - p2[0] > res[1] - res[0]:
                res = p2

        return s[res[0] : res[1]]

    def findPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return [l + 1, r]


"""
Solution 2:

DP 
Time Complexity: O(N^2)
Space complexity : O(N^2)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        res = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(0, n + 1 - l):
                if l == 1:
                    dp[i][i + l - 1] = True
                elif l == 2:
                    dp[i][i + l - 1] = s[i] == s[i + 1]
                else:
                    dp[i][i + l - 1] = (s[i] == s[i + l - 1]) and dp[i + 1][i + l - 2]

                if dp[i][i + l - 1]:
                    res = [i, i + l - 1]

        return s[res[0] : res[1] + 1]
