"""
Solution 1:

Binary Search + Rabin Karp

Time Complexity: O(N^2LogN)
Space complexity : O(1)
"""


class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        """
        binary search + rabin karp
        """
        if not s:
            return 0

        start, end = 1, len(s)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.canFind(s, mid):
                start = mid
            else:
                end = mid

        if self.canFind(s, end):
            return end

        if self.canFind(s, start):
            return start

        return 0

    def canFind(self, s, length):
        base = 31
        mod = 2**31 - 1
        h = 0
        seen = {}
        for i in range(len(s)):
            if i < length:
                h = (h * 31 + ord(s[i])) % mod
            else:
                h = ((h - ord(s[i - length]) * base ** (length - 1)) * base + ord(s[i])) % mod

            if h not in seen:
                seen[h] = [max(0, i - length + 1)]
            else:
                for idx in seen[h]:
                    if s[idx : idx + length] == s[i - length + 1 : i + 1]:
                        return True
                seen[h].append(i - length + 1)

        return False
