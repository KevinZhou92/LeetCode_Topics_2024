"""
Solution 1:

Brute Force with PrefixSum

Time Complexity: O(n^2)
Space complexity : O(n)
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]

        cnt = 0
        for i in range(1, n + 1):
            for j in range(0, i):
                if prefixSum[i] - prefixSum[j] == k:
                    cnt += 1

        return cnt


"""
Solution 2:

Prefix Sum + Hash Set

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        curSum = 0
        numSet = defaultdict(int)
        numSet[0] = 1
        cnt = 0
        for i in range(n):
            curSum += nums[i]
            if curSum - k in numSet:
                cnt += numSet[curSum - k]
            numSet[curSum] += 1

        return cnt
