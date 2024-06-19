"""
Solution 1:



Time Complexity: O(N * 2 ^N)
Space complexity : O(N)
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        res = []
        self.search(nums, 0, [], res)

        return res

    def search(self, nums, idx, cur, res):
        res.append(list(cur))

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            cur.append(nums[i])
            self.search(nums, i + 1, cur, res)
            cur.pop()
