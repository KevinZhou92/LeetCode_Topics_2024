"""
Solution 1:

Sliding Window

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        We can loop over chars in s2 and keep a window of s1's length,
        We will keep track of the occurence of each letter and check if
        the current window contains the same char like s1
        """
        if not s1 or not s2:
            return False

        need = {}
        seen = {}
        for char in s1:
            need[char] = need.get(char, 0) + 1

        valid = 0
        l = 0
        for r in range(len(s2)):
            cur = s2[r]
            seen[cur] = seen.get(cur, 0) + 1
            if cur in need and seen[cur] == need[cur]:
                valid += 1

            while r - l + 1 >= len(s1):
                if valid == len(need):
                    return True
                old = s2[l]
                if old in need:
                    if seen[old] == need[old]:
                        valid -= 1
                    seen[old] -= 1
                l += 1

        return False
