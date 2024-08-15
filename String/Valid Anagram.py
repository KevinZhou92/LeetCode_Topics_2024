"""
Solution 1:

Use map to count frequence

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}

        # Check if lengths are different
        if len(s) != len(t):
            return False

        # Count characters for s and t
        for i in range(len(s)):
            smap[s[i]] = smap.get(s[i], 0) + 1
            smap[t[i]] = smap.get(t[i], 0) - 1

        # Check if all values in the map are zero
        for count in smap.values():
            if count != 0:
                return False

        return True
