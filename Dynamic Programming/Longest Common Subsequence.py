"""
Solution 1:

DFS + Memorization

Time Complexity: O(m * n)
Space complexity : O(m * n)
"""

"""
Solution 1:

DFS + Memorization

Time Complexity: O(3^N)
Space complexity : O(N)
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        if len(text1) > len(text2):
            text2, text1 = text1, text2

        return self.search(text1, 0, text2, 0, {})

    def search(self, source, sI, target, tI, mem):
        if sI == len(source) or tI == len(target):
            mem[(sI, tI)] = 0
            return 0

        if (sI, tI) in mem:
            return mem[(sI, tI)]

        res = 0
        if source[sI] == target[tI]:
            res = self.search(source, sI + 1, target, tI + 1, mem) + 1
        else:
            res = max(
                self.search(source, sI, target, tI + 1, mem),
                self.search(source, sI + 1, target, tI, mem),
            )
        mem[(sI, tI)] = res

        return res
