"""
Solution 1:

Backtracking

Time Complexity: O(n*n!), we need O(n) work to copy each permutation into the resulting array
Space complexity : O(n)
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        visited = [False for _ in range(len(nums))]
        self.find_permutation(nums, [], res, visited)

        return res
    
    def find_permutation(self, nums, cur, res, visited):
        if len(cur) == len(nums):
            res.append([ele for ele in cur])
            return

        for idx in range(len(nums)):
            if visited[idx]:
                continue
            visited[idx] = True
            cur.append(nums[idx])
            self.find_permutation(nums, cur, res, visited)
            cur.pop()
            visited[idx] = False
        