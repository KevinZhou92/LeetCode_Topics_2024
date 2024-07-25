"""
Solution 1:

Binary Search

Notice only one number shows up multiple times so we want to make use of the condition

Time Complexity: O(NlogN)
Space complexity : O(1)
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0

        start, end = 1, len(nums)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.countSmaller(nums, mid) > mid:
                end = mid
            else:
                start = mid

        if self.countSmaller(nums, start) > start:
            return start

        return end

    def countSmaller(self, nums, target):
        cnt = 0
        for num in nums:
            if num > target:
                continue
            cnt += 1

        return cnt


"""
Solution 2:

Swap Elements to put element in its corresponding index

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0

        for i in range(len(nums)):
            curNum = nums[i]
            targetIndex = curNum
            while (
                targetIndex < len(nums) and curNum != i and nums[targetIndex] != curNum
            ):
                nums[i], nums[targetIndex] = nums[targetIndex], nums[i]
                curNum = nums[i]
                targetIndex = curNum

        res = 0
        for i in range(len(nums)):
            if i != nums[i]:
                res = nums[i]

        return res


"""
Solution 3:

Cycle detection algorithm

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = nums[0]
        fast = nums[0]
        while nums[fast] != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
