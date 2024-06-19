"""
Solution 1:

Backtracking

Time Complexity: O(N * 2^N)
Space complexity : O()
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        res = []
        self.search(s, 0, [], res)

        return res

    def search(self, s, start, cur, res):
        if start == len(s):
            res.append(list(cur))

        for i in range(start, len(s)):
            if not self.is_palindrome(s[start : i + 1]):
                continue
            cur.append(s[start : i + 1])
            self.search(s, i + 1, cur, res)
            cur.pop()

    def is_palindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            if start < end and s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True
