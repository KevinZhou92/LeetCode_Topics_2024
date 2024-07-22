"""
Solution 1:

Brute Force

Time Complexity: O(N^2)
Space complexity : O(1)
"""


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        res = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    res += 1

        return res
