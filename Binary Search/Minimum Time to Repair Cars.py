"""
Solution 1:

Binary Search

Time Complexity: O(N*logK) + O(NlogN)
Space complexity : O(1)
"""


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        if not ranks:
            return 0

        ranks.sort()
        start, end = 1, (cars // len(ranks) + 1) ** 2 * ranks[-1]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.canRepair(ranks, cars, mid):
                end = mid
            else:
                start = mid

        if self.canRepair(ranks, cars, start):
            return start

        return end

    def canRepair(self, ranks, cars, time):
        for r in ranks:
            fixedCar = math.floor(math.sqrt(time // r))
            cars -= fixedCar
            if cars <= 0:
                return True

        return True if cars <= 0 else False
