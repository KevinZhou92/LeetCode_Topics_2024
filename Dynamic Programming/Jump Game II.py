"""
Solution 1:


Time Complexity: O(n^2)
Space complexity : O(n)
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return False

        return self.search(nums, 0, {})

    def search(self, nums, i, mem):
        if i == len(nums) - 1:
            mem[i] = 0
            return 0

        if i in mem:
            return mem[i]

        res = sys.maxsize
        maxStep = min(i + nums[i], len(nums) - 1)
        for p in range(i + 1, maxStep + 1):
            res = min(res, 1 + self.search(nums, p, mem))

        mem[i] = res
        return res


"""
Solution 2:

DP

Time Complexity: O(n^2)
Space complexity : O(n)
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return False

        n = len(nums)
        dp = [sys.maxsize] * n
        dp[0] = 0
        for i in range(n):
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[-1]
