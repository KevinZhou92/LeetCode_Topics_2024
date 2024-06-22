"""
Solution 1:

Dynamic Programming
For each num, i check all the previous nums that is smaller than the current one
And use the know information from the previous smaller num to calculate the maximum
length i could get at current num


Time Complexity: O(n^2)
Space complexity : O(n)
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # for each num, i compare the result from a
        # smaller problem, for example,
        # 0 1 0 4 2 3
        # if i want to know the lis at 3, i just need to know what's the LIS
        # at 2 and what is the LIS at 0 and check from what sequence i can get the longest sequence
        if not nums:
            return 0

        dp = [1 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


"""
Solution 2:

DFS + Memorization

Time Complexity: O(n ^ 2)
Space complexity : O(n)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # for each num, i compare the result from a 
        # smaller problem, for example, 
        # 0 1 0 4 2 3  
        # if i want to know the lis at 3, i just need to know what's the LIS
        # at 2 and what is the LIS at 0 and check from what sequence i can get the longest sequence
        if not nums:
            return 0

        max_lis = 1
        self.mem = {}
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    max_lis = max(max_lis, 1 + self.search(nums, j))
        
        return max_lis

    def search(self, nums, idx):
        if idx in self.mem:
            return self.mem[idx]

        if idx == len(nums):
            return 0

        max_lis = 1
        for i in range(0, idx + 1):
            if nums[i] < nums[idx]:
                max_lis = max(max_lis, 1 + self.search(nums, i))
        
        self.mem[idx] = max_lis
        
        return max_lis
                    
        

        
                    
        

        