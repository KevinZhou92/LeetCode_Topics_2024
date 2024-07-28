"""
Solution 1:

Sliding Window
Be careful about edge case

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        l = 0
        maxCnt = 0
        cntOfZeros = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cntOfZeros += 1

            while l <= r and cntOfZeros > k:
                if nums[l] == 0:
                    cntOfZeros -= 1
                l += 1

            maxCnt = max(maxCnt, r - l + 1)

        return maxCnt
