"""
Solution 1:

Dynamic Programming

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [0] * n
        res = nums[0]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i] + dp[i - 1], nums[i])
            res = max(res, dp[i])

        return res
