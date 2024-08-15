"""
Solution 1:

Find the pattern, find out the first number that break the ascending order from right side, this number
will be exchanged with the first number that is greater than it from the right side

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums:
            return

        n = len(nums)
        r = n - 2
        # move from right
        while r >= 0:
            if nums[r] >= nums[r + 1]:
                r -= 1
            else:
                break
        if r < 0:
            self.reverse(nums, 0, n - 1)
        else:
            j = n - 1
            while j >= 0 and nums[j] <= nums[r]:
                j -= 1
            nums[r], nums[j] = nums[j], nums[r]
            self.reverse(nums, r + 1, n - 1)

        return

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
