"""
Solution 1:

Binary Search, TLE

Time Complexity: O(n^2LogN)
Space complexity : O(1)
"""


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums:
            return False

        array = []
        for idx, val in enumerate(nums):
            array.append([val, idx])

        array.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] >= nums[j]:
                    continue
                l, r = self.search(array, nums[i], nums[j])
                for k in range(l, r + 1):
                    if array[k][1] > i and array[k][1] > j:
                        return True

        return False

    def search(self, array, left, right):
        l, r = 0, 0
        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if array[mid][0] > left:
                end = mid
            else:
                start = mid

            if array[start][0] > left:
                l = start
            elif array[end][0] > left:
                l = end
            else:
                return [0, 0]

        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if array[mid][0] < right:
                start = mid
            else:
                end = mid

            if array[end][0] < right:
                r = end
            elif array[start][0] < right:
                r = start
            else:
                return [0, 0]

        return [l, r]


"""
Solution 2:

Monolith Stack

Time Complexity: O(N)
Space complexity : O(n)
"""


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        maintain a 32 pattern, find a 1 that meets the requirement
        """
        stack = []
        p2 = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < p2:
                return True
            while stack and stack[-1] < nums[i]:
                p2 = stack.pop()
            stack.append(nums[i])

        return False
