"""
Solution 1:

DFS + Memorization

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        damages = Counter(power).items()
        damages = sorted(damages)

        return self.dfs(0, damages, {})

    def dfs(self, idx, damages, memo):
        if idx == len(damages):
            return 0

        if idx in memo:
            return memo[idx]

        damage, cnt = damages[idx]

        nxt = idx
        while nxt < len(damages) and damages[nxt][0] - 2 <= damage:
            nxt += 1

        memo[idx] = max(
            self.dfs(idx + 1, damages, memo),
            damage * cnt + self.dfs(nxt, damages, memo),
        )

        return memo[idx]


"""
Solution 2:

DP

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        damages = Counter(power).items()
        damages = sorted(damages)

        dp = [0] * (len(damages) + 1)
        j = 0
        for i in range(1, len(damages) + 1):
            damage, cnt = damages[i - 1]
            while damages[j][0] < damage - 2:
                j += 1

            dp[i] = max(dp[i - 1], dp[j] + damage * cnt)

        return dp[len(damages)]
