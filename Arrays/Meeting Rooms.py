"""
Solution 1:

Sort and compare last end time of previous meeting with current meeting

Time Complexity: O(nlogn)
Space complexity : O(1)
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        intervals = sorted(intervals, key=lambda t: t[0])
        lastEnd = intervals[0][1]
        for interval in intervals[1:]:
            if lastEnd > interval[0]:
                return False
            lastEnd = interval[1]

        return True
