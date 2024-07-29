"""
Solution 1:

Binary Search

Time Complexity: O(NLogN)
Space complexity : O(1)
"""


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages:
            return 0

        ages.sort()
        rqMade = 0
        for i in range(len(ages)):
            cur = self.search(ages, ages[i])
            rqMade += cur

        return rqMade

    def search(self, ages, targetValue):
        lb = targetValue * 0.5 + 7
        ub = targetValue
        start, end = 0, len(ages) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            curAge = ages[mid]
            if curAge > lb:
                end = mid
            else:
                start = mid

        l = 0
        if ages[start] > lb:
            l = start
        elif ages[end] > lb:
            l = end
        else:
            return 0

        start, end = 0, len(ages) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            curAge = ages[mid]
            if curAge <= ub:
                start = mid
            else:
                end = mid

        r = 0
        if ages[end] <= ub:
            r = end
        elif ages[start] <= ub:
            r = start
        else:
            return 0

        return max(0, r - l)
