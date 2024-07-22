"""
Solution 1:

Use Binary Search to search possible size, find the minimum possible size

Time Complexity: O(NlogN)
Space complexity : O(1)
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        start, end = 1, len(nums)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.validSum(nums, mid, target):
                end = mid
            else:
                start = mid

        if self.validSum(nums, start, target):
            return start

        if self.validSum(nums, end, target):
            return end

        return 0

    def validSum(self, nums, size, target):
        sumValue = 0
        for r in range(0, len(nums)):
            if r < size:
                sumValue += nums[r]
            else:
                sumValue = sumValue - nums[r - size] + nums[r]

            if sumValue >= target:
                return True

        return False


"""
Solution 2:

Sliding Window

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        res = len(nums) + 1
        l = 0
        sumValue = 0
        for r in range(0, len(nums)):
            sumValue += nums[r]

            while sumValue >= target:
                res = min(res, r - l + 1)
                sumValue -= nums[l]
                l += 1

        return res if res != len(nums) + 1 else 0
