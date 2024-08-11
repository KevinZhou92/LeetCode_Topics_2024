"""
Solution 1:

DFS + Memo

Time Complexity: O(n^2)
Space complexity : O(n)
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        return self.search(nums, 0, {})

    def search(self, nums, idx, mem):
        if idx == len(nums) - 1:
            mem[idx] = True
            return True

        if idx in mem:
            return mem[idx]

        for i in range(idx + 1, min(nums[idx] + idx + 1, len(nums))):
            if self.search(nums, i, mem):
                mem[idx] = True
                return True

        mem[idx] = False
        return False


"""
Solution 2:

Dynamic Programing

Time Complexity: O(n^2)
Space complexity : O(n)
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                return False
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                dp[j] = True

        return dp[-1]


"""
Solution 3:

Greedy

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        lastPos = 0
        for i in range(len(nums)):
            if i > lastPos:
                return False
            lastPos = max(lastPos, i + nums[i])

        return lastPos >= len(nums) - 1
