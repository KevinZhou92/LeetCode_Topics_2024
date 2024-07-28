"""
Solution 1:

Binary Search(Not efficient one)
For val between 1 and max Value, search the array to see it it meets the requirement


Time Complexity: O(NlogD)
Space complexity : O(1)
"""


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        if not nums:
            return -1

        nums.sort()
        start, end = 0, max(nums)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.search(nums, mid) >= mid:
                start = mid
            else:
                end = mid

        if self.search(nums, start) == start:
            return start

        if self.search(nums, end) == end:
            return end

        return -1

    def search(self, nums, target):
        return sum([1 for n in nums if n >= target])


"""
Solution 2:

Binary Search(Improved)


Time Complexity: O(NlogN)
Space complexity : O(1)
"""


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        if not nums:
            return -1

        nums.sort()
        n = len(nums)
        for i in range(1, n + 1):
            if not self.search(nums, i):
                continue
            return i

        return -1

    def search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] >= target:
            return len(nums) - start == target

        if nums[end] < target:
            return len(nums) - end - 1 == target

        return (len(nums) - end) == target


"""
Solution 3:

Counting Sort.

The maximum possible value is N, length of array. We just need to count the reqs of all elements and 
for each possible value we count how many elements are greater than the value

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        if not nums:
            return -1

        nums.sort()
        n = len(nums)
        freqs = [0] * (n + 1)
        for i in range(len(nums)):
            freqs[min(nums[i], n)] += 1

        cnt = 0
        for i in range(n, -1, -1):
            cnt += freqs[i]
            if cnt == i:
                return i

        return -1
