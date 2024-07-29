"""
Solution 1:

Binary Search

Time Complexity: O(nlogn + mlogm)
Space complexity : O(1)
"""


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        start, end = 0, max(max(heaters), max(houses))
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.canWork(houses, heaters, mid):
                end = mid
            else:
                start = mid

        if self.canWork(houses, heaters, start):
            return start

        return end

    def canWork(self, houses, heaters, r):
        hIndex = 0
        heatIndex = 0
        while hIndex < len(houses) and heatIndex < len(heaters):
            if (
                heaters[heatIndex] - r <= houses[hIndex]
                and heaters[heatIndex] + r >= houses[hIndex]
            ):
                hIndex += 1
            else:
                heatIndex += 1

        return hIndex == len(houses)


"""
Solution 2:

One Pointer

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = 0
        houses = sorted(houses)
        heaters = sorted(heaters)
        i = 0
        for house in houses:
            while i < len(heaters) - 1 and abs(house - heaters[i + 1]) <= abs(
                house - heaters[i]
            ):
                i += 1
            res = max(res, abs(house - heaters[i]))

        return res
