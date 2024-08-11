"""
Solution 1:

Find the max diff between current day's price and minimum price so far

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        curMin = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            curPrice = prices[i]
            if curPrice < curMin:
                curMin = curPrice
            maxProfit = max(maxProfit, curMax - curMin)
            if curPrice < curMin:
                curMax = curPrice
                curMin = curPrice

        return maxProfit
