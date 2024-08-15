"""
Solution 1:

Array Operation

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []
        idx = 0
        while idx < len(intervals) and newInterval[0] > intervals[idx][1]:
            res.append(intervals[idx])
            idx += 1

        while idx < len(intervals) and newInterval[1] >= intervals[idx][0]:
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1
        res.append(newInterval)

        while idx < len(intervals):
            res.append(intervals[idx])
            idx += 1

        return res
