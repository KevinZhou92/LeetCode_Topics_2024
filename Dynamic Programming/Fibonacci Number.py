"""
Solution 1:

Recursion

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)


"""
Solution 2:

Iteration

Time Complexity: O(n)
Space complexity : O(1)
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        p1, p2 = 0, 1
        idx = 1
        while idx < n:
            tmp = p1 + p2
            p1 = p2
            p2 = tmp
            idx += 1

        return p2
