"""
Solution 1:

Two Pointer and Operation Sub-optimal

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        p1, p2 = 0, 0
        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1

        while p1 < len(nums):
            nums[p1] = 0
            p1 += 1

        return
"""
Solution 2:

A tiny variation

Time Complexity: O(N)
Space complexity : O(1)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        p1, p2 = 0, 0
        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            p2 += 1
        

        return
        
