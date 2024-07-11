"""
Solution 1:

Use a hashmap to keep track of sequences that are visited, if we seen the same sequence again,
we will add it to the resulting list.


Time Complexity: O((N - 10) * 10)
Space complexity : O(N)
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        seen = {}
        l, r = 0, 9
        while r < len(s):
            cur = s[l : r + 1]
            if cur in seen and seen[cur] < 2:
                res.append(cur)
            seen[cur] = seen.get(cur, 0) + 1
            r += 1
            l += 1

        return res
