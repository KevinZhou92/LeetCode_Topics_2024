"""
Solution 1:

Use a hashmap to keep track of sequences that are visited, if we seen the same sequence again,
we will add it to the resulting list.


Time Complexity: O((N - 10) * 10)
Space complexity : O((N - 10) * 10)
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

"""
Solution 1:

Rabin-Karp(rolling hash algorithm)

Time Complexity: O(N)
Space complexity : O(N - L)
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s:
            return []

        base = 31
        mod = float('inf')
        hashValue = 0
        seen = {}
        res = set()
        right = 0
        while right < len(s):
            if right <= 9:
                hashValue = (hashValue * base + ord(s[right])) % mod
            else:
                hashValue = ((hashValue - 31 ** 9 * ord(s[right - 10])) * base + ord(s[right])) % mod
            if hashValue not in seen:
                seen[hashValue] = [right - 9]
            else:
                res.add(s[right - 9:right + 1])
            right += 1

        return res

        
