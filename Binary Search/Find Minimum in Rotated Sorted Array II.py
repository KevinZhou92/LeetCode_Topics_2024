"""
Solution 1:

Binary Search

Compare with the end element

Time Complexity: O()
Space complexity : O()
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
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:
                end -= 1

        if nums[start] < nums[end]:
            return nums[start]

        return nums[end]

"""
Solution 2:


Time Complexity: O(N)
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
            if nums[start] < nums[mid]:
                if nums[mid] <= nums[end]:
                    end = mid
                else:
                    start = mid
            elif nums[start] > nums[mid]:
                end = mid
            else:
                start += 1

        if nums[start] > nums[end]:
            return nums[end]

        return nums[start]