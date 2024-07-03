"""
Solution 1:

https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
Check if a num is prime and mark all multiple of this num to be not prime number

Check count of primes after the calculations

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        res = [False, False] + [True] * (n - 2)
        for num in range(2, int(sqrt(n)) + 1):
            if not res[num]:
                continue
            for multiple in range(num * num, n, num):
                res[multiple] = False

        return sum(res)
