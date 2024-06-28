"""
Solution 1:

Binary Search to find:
1. Leftmost index
2. Rightmost index

Time Complexity: O(NlogN)
Space complexity : O(1)
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search to find left and right position
        if not nums:
            return [-1, -1]

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            l = start
        elif nums[end] == target:
            l = end
        else:
            return [-1, -1]

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            r = end
        elif nums[start] == target:
            r = start
        else:
            return [-1, -1]

        return [l, r]
