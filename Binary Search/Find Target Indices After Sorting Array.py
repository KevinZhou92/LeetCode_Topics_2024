"""
Solution 1:

Find first and last element

Time Complexity: O(LogN)
Space complexity : O(1)
"""


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        nums.sort()
        res = []
        l, r = 0, 0
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
            return []

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            r = end
        else:
            r = start

        for i in range(l, r + 1):
            res.append(i)

        return res
