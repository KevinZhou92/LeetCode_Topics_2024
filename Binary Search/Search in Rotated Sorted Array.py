"""
Solution 1:

Search in rotated sorted arrary.

The arary can be split to two parts by the mid element, one sorted subarray and one non-sorted subarray
We can

Alwasy check the sorted section to see if target falls in the range and then we can determine which half to retain

Time Complexity: O(logN)
Space complexity : O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[start] < nums[mid]:
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1
