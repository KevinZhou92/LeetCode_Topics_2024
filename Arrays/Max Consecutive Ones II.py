"""
Solution 1:

Two Pointers, use a hashmap to count freqs of 0s

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = {}
        l = 0
        maxCnt = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                seen[0] = seen.get(0, 0) + 1
            while l < r and seen.get(0, 0) > 1:
                if nums[l] == 0 and 0 in seen:
                    seen[0] -= 1
                l += 1

            maxCnt = max(maxCnt, r - l + 1)

        return maxCnt
