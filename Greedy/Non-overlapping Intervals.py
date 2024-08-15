"""
Solution 1:

Greedy.

Sort interval by end time, we always want to pick the interval ends earlier
to avoid conflicting with future events

Time Complexity: O(nlogn)
Space complexity : O()
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda t: t[1])
        ans = 0
        prev = -sys.maxsize
        for interval in intervals:
            if interval[0] < prev:
                ans += 1
            else:
                prev = interval[1]

        return ans
