"""
Solution 1:

First use binary search to find search space, then apply binary search in search space

Time Complexity: O(log T) T is index of target value
Space complexity : O(1)
"""

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:


class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        end = 1
        val = reader.get(end)
        start, end = 0, 1
        while reader.get(end) < target:
            start = end
            end <<= 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) <= target:
                start = mid
            else:
                end = mid

        if reader.get(start) == target:
            return start

        if reader.get(end) == target:
            return end

        return -1
