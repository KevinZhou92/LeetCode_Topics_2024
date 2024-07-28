"""
Solution 1:

One Pass

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cnt = 0
        maxCnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                maxCnt = max(maxCnt, cnt)
                cnt = 0

        return maxCnt


"""
Solution 2:
Two Pointers

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = r = 0
        maxCnt = 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
                maxCnt = max(maxCnt, r - l)
            else:
                l = r
                l += 1
                r += 1

        return maxCnt


"""
Solution 3:

Two Pointers

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = 0
        maxCnt = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                maxCnt = max(maxCnt, r - l + 1)
            else:
                l = r + 1

        return maxCnt
