"""
Solution 1:

Binary Search

Time Complexity: O(logN)
Space complexity : O(1)
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        binary search,
        compare mid with mid + 1
        if mid < mid + 1, we are still on up slope, start = mid
        else:
            end. = mid
        """
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] < arr[mid + 1]:
                start = mid
            else:
                end = mid

        if arr[end] < arr[start]:
            return start

        return end
