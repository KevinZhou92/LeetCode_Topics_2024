"""
Solution 1:

Binary search

Time Complexity: O(logN)
Space complexity : O(1)
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[end] < target:
            return end + 1

        if nums[start] >= target:
            return start

        return start + 1
