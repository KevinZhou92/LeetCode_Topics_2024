"""
Solution 1:

Two Pointers

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        p1, p2 = 0, 0
        while p2 < len(nums):
            if p2 > 0 and nums[p2] == nums[p2 - 1]:
                p2 += 1
            else:
                nums[p1] = nums[p2]
                p1 += 1
                p2 += 1

        return p1
