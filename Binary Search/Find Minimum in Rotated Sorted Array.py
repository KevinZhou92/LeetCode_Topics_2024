"""
Solution 1:

Modified Binary Search

Only edge case is that the array is not rotated. So in this case, start < mid < end
Else:
We can always chedck if nums[mid] < nums[start], which means the rotation point is between
[start, mid], vice versa.

Time Complexity: O(logN)
Space complexity : O(1)
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        binary search to find the element where ele > right and ele > left
        """
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[start] < nums[mid] and nums[mid] < nums[end]:
                end = mid
            elif nums[start] > nums[mid]:
                end = mid
            else:
                start = mid

        if nums[start] < nums[end]:
            return nums[start]

        return nums[end]


"""
Solution 2:

Add special case handle for non-rotated array

Time Complexity: O(logN)
Space complexity : O(1)
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        binary search to find the element where ele > right and ele > left
        """
        if not nums:
            return -1

        if nums[0] < nums[-1]:
            return nums[0]

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[start]:
                end = mid
            else:
                start = mid

        if nums[start] < nums[end]:
            return nums[start]

        return nums[end]
