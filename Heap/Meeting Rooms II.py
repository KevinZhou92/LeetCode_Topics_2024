"""
Solution 1:

Imagine we are scanning over the sorted meeting(by start time), out goal
is to find out at maximum how many meetings are overlapping

Time Complexity: O(nlogn)
Space complexity : O(n)
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        ts = []
        for start, end in intervals:
            ts.append((start, 1))
            ts.append((end, -1))

        ts.sort()
        ans = 0
        cnt = 0
        for t in ts:
            cnt += t[1]
            ans = max(ans, cnt)

        return ans
