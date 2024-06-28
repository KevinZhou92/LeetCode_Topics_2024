"""
Solution 1:

Sliding Window, keep track of seen characters

Time Complexity: O(M)
Space complexity : O(K)
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        res = []
        need = {}
        seen = {}
        for char in p:
            need[char] = need.get(char, 0) + 1

        l = 0
        valid = 0
        for r in range(len(s)):
            cur = s[r]
            if cur in need:
                seen[cur] = seen.get(cur, 0) + 1
            if cur in need and seen[cur] == need[cur]:
                valid += 1

            while r - l + 1 >= len(p):
                if valid == len(need):
                    res.append(l)
                d = s[l]
                l += 1
                if d in need:
                    if seen[d] == need[d]:
                        valid -= 1
                    seen[d] -= 1

        return res
