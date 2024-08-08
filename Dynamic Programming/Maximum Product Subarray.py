"""
Solution 1:

DP.

Maintain minProduct and maxProduct at the same time.

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tmpMin, tmpMax = nums[0], nums[0]
        globalMax = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            tmp = tmpMin
            tmpMin = min(cur, tmpMin * cur, tmpMax * cur)
            tmpMax = max(cur, tmp * cur, tmpMax * cur)
            globalMax = max(globalMax, cur, tmpMin, tmpMax)

        return globalMax
