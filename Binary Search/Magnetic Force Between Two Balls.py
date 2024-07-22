"""
Solution 1:

Binary Search
1. Define Search Space
2. Do binary search

Time Complexity: O(Nlog(K/M))
Space complexity : O()
"""


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        if not position:
            return 0

        position.sort()
        start, end = 1, position[-1] // (m - 1) + 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.canPlace(position, m, mid):
                start = mid
            else:
                end = mid

        if self.canPlace(position, m, end):
            return end

        return start

    def canPlace(self, position, m, target):
        prev = position[0]
        m -= 1
        minValue = sys.maxsize
        for i in position[1:]:
            if i - prev >= target and m > 0:
                prev = i
                minValue = min(minValue, i - prev)
                m -= 1

        return True if m == 0 else False
