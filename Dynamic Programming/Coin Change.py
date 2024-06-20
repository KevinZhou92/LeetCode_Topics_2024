"""
Solution 1:

DFS

!Time Limit Exceeded!

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1

        return self.search(coins, amount, 0)

    def search(self, coins, amount, count):
        if amount == 0:
            return count

        min_count = sys.maxsize
        for coin in coins:
            if amount - coin < 0:
                continue
            coin_count = self.search(coins, amount - coin, count + 1)
            if coin_count != -1:
                min_count = min(min_count, coin_count)

        return -1 if min_count == sys.maxsize else min_count


"""
Solution 2:

DFS + Memorization
!Memory Limit Exceeded!

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1

        memories = {}

        return self.search(coins, amount, 0, memories)

    def search(self, coins, amount, count, memories):
        if amount == 0:
            return count

        if (amount, count) in memories:
            return memories[(amount, count)]

        min_count = sys.maxsize
        for coin in coins:
            if amount - coin < 0:
                continue
            coin_count = self.search(coins, amount - coin, count + 1, memories)
            if coin_count != -1:
                min_count = min(min_count, coin_count)

        min_count = -1 if min_count == sys.maxsize else min_count
        memories[(amount, count)] = min_count

        return min_count
