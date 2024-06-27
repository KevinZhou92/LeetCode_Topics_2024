"""
Solution 1:

A simple idea is to go through from the start to end, and check if the actual capacity exceeds capacity.
To know the actual capacity, we just need the number of passengers changed at each timestamp.

Time Complexity: O(NlogN)
Space complexity : O(N)
"""


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True

        timeStamps = []
        for trip in trips:
            timeStamps.append((trip[1], trip[0]))
            timeStamps.append((trip[2], -trip[0]))

        timeStamps.sort()
        cur = 0
        for ts in timeStamps:
            cur += ts[1]
            if cur > capacity:
                return False

        return True
