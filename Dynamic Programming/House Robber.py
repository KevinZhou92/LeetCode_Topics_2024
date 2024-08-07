"""
Solution 1:

DP

If you rob current house, you can't rob adjacent one, the max would be cur house + max output from
robbing (i - 2)th house

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]
