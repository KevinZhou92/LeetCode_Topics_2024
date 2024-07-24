"""
Solution 1:

Binary Search

Time Complexity: O(NlogN)
Space complexity : O(1)
"""


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        if not grades:
            return 0

        grades.sort()

        start, end = 1, len(grades)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.canFormGroups(grades, mid):
                start = mid
            else:
                end = mid

        if self.canFormGroups(grades, end):
            return end

        return start

    def canFormGroups(self, grades, groupNeeded):
        prevCnt = 1
        prevSum = grades[0]
        cnt = 0
        curSum = 0
        groupFormed = 1
        for i in range(1, len(grades)):
            curSum += grades[i]
            cnt += 1
            if cnt > prevCnt and curSum > prevSum:
                prevCnt = cnt
                prevSum = curSum
                cnt = 0
                curSum = 0
                groupFormed += 1

        return groupFormed >= groupNeeded
