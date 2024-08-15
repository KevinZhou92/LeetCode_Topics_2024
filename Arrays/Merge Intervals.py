"""
Solution 1:

Sort and merge overlapping intervals

Time Complexity: O(nlogn)
Space complexity : O(n)
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda interval: interval[0])
        res = []
        curInterval = intervals[0]
        for interval in intervals[1:]:
            # merge
            if interval[0] <= curInterval[1]:
                curInterval = [
                    min(interval[0], curInterval[0]),
                    max(interval[1], curInterval[1]),
                ]
            else:
                res.append(curInterval)
                curInterval = interval

        res.append(curInterval)

        return res
