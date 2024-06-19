"""
Solution 1:

Backtracking + Pruning

Sort the array.

During the search, if current ele is the same like previous element and previous element is not
visited, this means we have already calculated the permutation with the current element in this recursion stack
and there is not need to calculate it again.

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        nums.sort()
        visited = [False for _ in nums]
        self.search(nums, visited, [], res)

        return res

    def search(self, nums, visited, cur, res):
        if len(cur) == len(nums):
            res.append(list(cur))
            return

        for idx in range(len(nums)):
            if visited[idx]:
                continue
            if idx > 0 and not visited[idx - 1] and nums[idx] == nums[idx - 1]:
                continue
            cur.append(nums[idx])
            visited[idx] = True
            self.search(nums, visited, cur, res)
            cur.pop()
            visited[idx] = False
