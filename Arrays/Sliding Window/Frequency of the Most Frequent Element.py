"""
Solution 1:

Sliding Window

Be flexible about how we are dealing with subproblems. 

In this question, we are essentially try to split k increase among X elements.

We convert to use multiplication to compare the sum val and expected val.

Time Complexity: O(n)
Space complexity : O(1)
"""


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        nums.sort()
        maxFreq = 0
        l = 0
        sumVal = 0
        for r in range(len(nums)):
            target = nums[r]
            sumVal += target

            while l < r and sumVal + k < target * (r - l + 1):
                sumVal -= nums[l]
                l += 1
            maxFreq = max(maxFreq, r - l + 1)

        return maxFreq
