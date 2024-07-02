"""
Solution 1:

Brute Force
Simulate the process of toggle light switches

Time Complexity: O(N^2)
Space complexity : O(N)
"""
class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulbs = {i : 0 for i in range(1, n + 1)}

        for rnd in range(1, n + 1):
            for bulb in bulbs:
                if rnd == 1:
                    bulbs[bulb] = 1
                elif rnd == 2 and bulb % 2 == 0:
                    bulbs[bulb] = 0
                else:
                    if bulb % rnd == 0:
                        bulbs[bulb] = 1 - bulbs[bulb]

        return sum([v for k, v in bulbs.items()])
                    
                    
"""
Solution 2:

Math
Only bulbs that are toggled an odd number of times will remain on.
Perfect squares have odd and non-perfect squares have an even number of factors.

We just need to find out how many perfect squares are there under N

Time Complexity: O(1)
Space complexity : O1)
"""
return int(sqrt(n))