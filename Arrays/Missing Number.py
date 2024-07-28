"""
Solution 1:

HashSet

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set()
        for num in nums:
            seen.add(num)

        res = 0
        for i in range(len(nums) + 1):
            if i not in seen:
                res = i

        return res
