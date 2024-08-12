"""
Solution 1:

HashSet 

Time Complexity: O(N)
Space complexity : O(N)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        res = 1
        for num in nums:
            if num not in numSet:
                continue
            if len(numSet) == 0:
                break
            curRes = 1
            curNum = num
            numSet.remove(curNum)
            while curNum - 1 in numSet:
                curRes += 1
                curNum -= 1
                numSet.remove(curNum)
            curNum = num
            while curNum + 1 in numSet:
                curRes += 1
                curNum += 1
                numSet.remove(curNum)
            res = max(res, curRes)
        
        return res
    
"""
Solution 2:

Hash Set + Start counting from the first number of current sequence

Time Complexity: O(N)
Space complexity : O(N)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        res = 1
        for num in nums:
            if num - 1 in numSet:
                continue
            
            curRes = 1
            curNum = num
            while curNum + 1 in numSet:
                curNum += 1
                curRes += 1
            
            res = max(res, curRes)

        return res