"""
Solution 1:

DFS. 

The recursion is defined as:
For each char in source string, trying to match it with the current chat in target string.

Time Complexity exceeded!

Time Complexity: O(MN * M)
Space complexity : O()
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        self.mem = {}
        return self.search(s, 0, t, 0)

    def search(self, s, s_idx, t, t_idx):
        if t_idx == len(t):
            return 1

        if (s_idx, t_idx) in self.mem:
            return self.mem[(s_idx, t_idx)]

        res = 0
        for i in range(s_idx, len(s)):
            if s[i] != t[t_idx]:
                continue
            res += self.search(s, i + 1, t, t_idx + 1)

        self.mem[(s_idx, t_idx)] = res
        return res


"""
Solution 2:
DFS.
For each char in target string, we either match it with current char in source string or not match it.

This solution greatly reduced the time complexity!

Time Complexity: O(MN)
Space complexity : O(N)
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        self.mem = {}
        return self.search(s, 0, t, 0)

    def search(self, s, s_idx, t, t_idx):
        if t_idx == len(t):
            return 1

        if s_idx == len(s):
            return 0

        if (s_idx, t_idx) in self.mem:
            return self.mem[(s_idx, t_idx)]

        res = 0
        if s[s_idx] == t[t_idx]:
            # if s[i] == t[j], we can either
            # 1. match i and j, and move each pointer to next char in each string for next match
            # 2. don't match i and j, so that the same char in S can be used to match t
            # For example: 'aab' and 'ab', we can skip the match at index 0 and move s's pointer to next char
            # which is also 'a' and can be a match as well
            res = self.search(s, s_idx + 1, t, t_idx) + self.search(
                s, s_idx + 1, t, t_idx + 1
            )

        if s[s_idx] != t[t_idx]:
            res = self.search(s, s_idx + 1, t, t_idx)

        self.mem[(s_idx, t_idx)] = res

        return res
