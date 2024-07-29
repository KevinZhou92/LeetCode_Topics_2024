"""
Solution 1:

SortedList + Binary Search

Time Complexity: O(NlogN)
Space complexity : O(N)
"""

from sortedcontainers import SortedList


class MyCalendar:

    def __init__(self):
        self.meetings = SortedList()

    def book(self, start: int, end: int) -> bool:
        if not self.meetings:
            self.meetings.add([start, end])
            return True

        l, r = 0, len(self.meetings) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.meetings[mid][0] >= start:
                r = mid
            else:
                l = mid

        if self.meetings[l][0] >= end:
            self.meetings.add([start, end])
            return True

        if self.meetings[r][1] <= start:
            self.meetings.add([start, end])
            return True

        if self.meetings[l][1] <= start and self.meetings[r][0] >= end:
            self.meetings.add([start, end])
            return True

        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
