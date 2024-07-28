"""
Solution 1:

Sort both arrays and start simulating the process and then capture the latest time for all bus to
take possible passengers, we can then find the latest time backward.

We can use binary search to optime the process of finding availabe time from the latest time from passenger
departure time.

Time Complexity: O(M + N)
Space complexity : O(N)
"""


class Solution:
    def latestTimeCatchTheBus(
        self, buses: List[int], passengers: List[int], capacity: int
    ) -> int:
        passengers.sort()
        buses.sort()

        pIndex = 0
        for t in buses:
            cap = capacity
            while pIndex < len(passengers) and passengers[pIndex] <= t and cap > 0:
                cap -= 1
                pIndex += 1

        latest = t if cap > 0 else passengers[pIndex - 1]
        bannedTime = set(passengers)
        while latest in bannedTime:
            latest -= 1

        return latest
