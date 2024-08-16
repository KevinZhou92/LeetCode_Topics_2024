"""
Solution 1:

3 pointers

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        """
        2 1 1 0 0 2
        """
        n = len(nums)
        r, w, b = 0, 0, n - 1
        while w <= b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
            else:
                w += 1

        return
