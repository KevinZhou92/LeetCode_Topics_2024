"""
Solution 1:

Brute-Force DFS

Time Complexity: O(N!)
Space complexity : O(N)
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False

        totalVal = sum(nums)
        if totalVal % 2 != 0:
            return False

        targetVal = totalVal // 2
        visited = [False] * len(nums)
        return self.search(nums, visited, targetVal)

    def search(self, nums, visited, targetVal):
        if targetVal == 0:
            return True

        for i in range(len(nums)):
            if visited[i] or nums[i] > targetVal:
                continue
            visited[i] = True
            if self.search(nums, visited, targetVal - nums[i]):
                return True
            visited[i] = False

        return False


"""
Solution 2:

DFS + Memorization

Time Complexity: O(m * n), Let n be the number of array elements and m be the targetVal.
Space complexity : O(m * n)
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False

        totalVal = sum(nums)
        if totalVal % 2 != 0:
            return False

        targetVal = totalVal // 2
        return self.search(nums, 0, targetVal, {})

    def search(self, nums, idx, targetVal, mem):
        if targetVal == 0:
            mem[(idx, targetVal)] = True
            return True

        if idx == len(nums) or targetVal < 0:
            mem[(idx, targetVal)] = False
            return False

        if (idx, targetVal) in mem:
            return mem[(idx, targetVal)]

        res = self.search(nums, idx + 1, targetVal - nums[idx], mem) or self.search(
            nums, idx + 1, targetVal, mem
        )
        mem[(idx, targetVal)] = res

        return res


"""
Solution 3:

DP

For num, check each possible target val and see if the target val can be achieved

Time Complexity: O(m * n)
Space complexity : O(m)
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False

        totalVal = sum(nums)
        if totalVal % 2 != 0:
            return False

        targetVal = totalVal // 2
        dp = [False] * (targetVal + 1)
        # dp[i] represent if we can make such target value with elements in nums
        dp[0] = True
        for num in nums:
            for target in range(targetVal, num - 1, -1):
                dp[target] = dp[target - num] or dp[target]

        return dp[targetVal]
