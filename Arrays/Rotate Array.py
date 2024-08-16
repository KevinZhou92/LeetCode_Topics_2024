"""
Solution 1:

Brute Force

Time Complexity: O(n * k)
Space complexity : O(1)
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        for _ in range(k):
            prev = nums[-1]
            for i in range(len(nums)):
                nums[i], prev = prev, nums[i]

        return


"""
Solution 2:

Extra space

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        n = len(nums)
        tmp = [0] * n
        for i in range(n):
            tmp[(i + k) % n] = nums[i]

        nums[:] = tmp

        return
