"""
Solution 1:

DFS + Memorization

Only 3 cases:
1. Insert
2. Replace
3. Delete

We just need to be careful about when two chars are the same so we don't need to do any operation.

Time Complexity: O(L1 * L 2)
Space complexity : O(max(L1, L2))
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0

        return self.search(word1, 0, word2, 0, {})

    def search(self, word1, idx1, word2, idx2, map):
        if idx1 == len(word1):
            return len(word2) - idx2

        if idx2 == len(word2):
            return len(word1) - idx1

        if (idx1, idx2) in map:
            return map[(idx1, idx2)]

        res = sys.maxsize
        """
        insert
        delete
        replace
        """
        if word1[idx1] == word2[idx2]:
            res = min(res, self.search(word1, idx1 + 1, word2, idx2 + 1, map))
        else:
            res = min(res, 1 + self.search(word1, idx1, word2, idx2 + 1, map))
            res = min(res, 1 + self.search(word1, idx1 + 1, word2, idx2, map))
            res = min(res, 1 + self.search(word1, idx1 + 1, word2, idx2 + 1, map))

        map[(idx1, idx2)] = res

        return res

"""
Solution 2:

DP

Time Complexity: O(L1 * L2)
Space complexity : O(L1 * L2)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        dp = [[sys.maxsize] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len2 + 1):
            dp[0][i] = i
        
        for i in range(len1 + 1):
            dp[i][0] = i

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                dp[i][j] = min(
                    dp[i][j],
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + 1
                )

        return dp[len1][len2]
        