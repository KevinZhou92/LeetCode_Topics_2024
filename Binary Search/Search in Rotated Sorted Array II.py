"""
Solution 1:

Due to duplicate arrary, we need to check if start and mid element are the same, if so,
we move start indext one step further.

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[start] < nums[mid]:
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            elif nums[start] > nums[mid]:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
            else:
                start += 1

        if nums[start] == target or nums[end] == target:
            return True

        return False


