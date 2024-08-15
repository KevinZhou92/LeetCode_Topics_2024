"""
Solution 1:

DFS + Memorization

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        return self.decode(s, 0, {})

    def decode(self, s, idx, mem):
        if idx == len(s):
            return 1

        if idx in mem:
            return mem[idx]

        curNum = 0
        cnt = 0
        for i in range(idx, len(s)):
            curNum = curNum * 10 + int(s[i])
            if curNum <= 0 or curNum > 26:
                break
            cnt += self.decode(s, i + 1, mem)
        mem[idx] = cnt

        return cnt
