"""
Solution 1:

DFS + Memorization, split in each position in the word

Time Complexity: O(N * m * k)
Space complexity : O(N)
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False

        wordDict = set(wordDict)

        return self.search(s, 0, wordDict, {})

    def search(self, s, idx, wordDict, mem):
        if idx == len(s):
            return True

        if idx in mem:
            return mem[idx]

        mem[idx] = False
        for i in range(idx, len(s)):
            if s[idx : i + 1] in wordDict and self.search(s, i + 1, wordDict, mem):
                mem[idx] = True

        return mem[idx]


"""
Solution 1:
DFS Top Down + Memo

Time Complexity: O(n * m * k)
Space complexity : O(n)
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False

        return self.search(s, len(s) - 1, wordDict, {})

    def search(self, s, idx, wordDict, memo):
        if idx == -1:
            return True

        if idx in memo:
            return memo[idx]

        for word in wordDict:
            length = len(word)
            if idx + 1 < length:
                continue
            if s[idx - length + 1 : idx + 1] == word and self.search(
                s, idx - length, wordDict, memo
            ):
                memo[idx] = True
                return True
        memo[idx] = False

        return False


"""
Solution 3:

DP

Time Complexity: O(n * m * k)
Space complexity : O(n)
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False

        n = len(s)
        dp = [False] * (n)
        for i in range(n):
            for word in wordDict:
                length = len(word)
                if i < length - 1:
                    continue
                if s[i - length + 1 : i + 1] == word and (
                    i == length - 1 or dp[i - length]
                ):
                    dp[i] = True

        return dp[-1]
