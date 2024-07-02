"""
Solution 1:

You can always win a Nim game if the number of stones n in the pile is not divisible by 4.

Time Complexity: O(1)
Space complexity : O(1)
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


"""
Solution 1:

Iterative Solution

Imagine P1 pick 1 or 2 or 3 stones first and convert the game to 

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <= 3:
            return True

        res = [False for _ in range(n + 1)]
        res[0] = True
        res[1] = True
        res[2] = True
        res[3] = True

        for i in range(4, n + 1):
            res[i] = not (res[i - 1] and res[i - 2] and res[i - 3])

        return res[n]
