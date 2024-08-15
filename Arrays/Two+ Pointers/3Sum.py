"""
Solution 1:

Fix one number and convert it to a two-pointer issue

Time Complexity: O(n^2)
Space complexity : O(n)
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        res = []
        idx = 0
        while idx < len(nums) - 2:
            if idx > 0 and nums[idx] == nums[idx - 1]:
                idx += 1
                continue
            target = -nums[idx]
            l, r = idx + 1, len(nums) - 1
            while l < r:
                while len(nums) > l > idx + 1 and nums[l] == nums[l - 1]:
                    l += 1
                if l >= r:
                    break
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    r -= 1
            idx += 1

        return res


"""
Solution 2:

Use it with a hashset

Time Complexity: O(n^2)
Space complexity : O(n)
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.twoSum(nums, nums[i], i + 1, res)

        return res

    def twoSum(self, nums, firstNum, l, res):
        seen = set()
        j = l
        while j < len(nums):
            target = -nums[j] - firstNum
            if target in seen:
                res.append([firstNum, target, nums[j]])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1

        return
