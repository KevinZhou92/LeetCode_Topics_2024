"""
Solution 1:

Binary Search Template

Time Complexity: O(logN)
Space complexity : O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
            else:
                return mid

        if nums[l] == target:
            return l

        if nums[r] == target:
            return r

        return -1


"""
Solution 1:

DFS

Time Complexity: O(logN)
Space complexity : O(N)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        return self.dfs(nums, 0, len(nums) - 1, target)

    def dfs(self, nums, l, r, target):
        if l > r:
            return -1
        mid = l + (r - l) // 2
        if nums[mid] < target:
            return self.dfs(nums, mid + 1, r, target)
        elif nums[mid] > target:
            return self.dfs(nums, l, mid - 1, target)
        else:
            return mid
