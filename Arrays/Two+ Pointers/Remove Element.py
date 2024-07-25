"""
Solution 1:

Two pointer from start and end

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        p1, p2 = 0, len(nums)
        while p1 < p2:
            if nums[p1] == val:
                nums[p1] = nums[p2 - 1]
                p2 -= 1
            else:
                p1 += 1

        return p2
