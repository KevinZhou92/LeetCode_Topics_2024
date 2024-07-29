"""
Solution 1:

Brute Force

Time Complexity: O(n^2)
Space complexity : O(1)
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        s = ""
        start = 1
        while len(s) < n:
            s += str(start)
            start += 1

        return int(s[n - 1])


"""
Solution 1:

Count total digits for different digit length.
For example:
single digit number has 9
double digits number has 90 total digits
tripple digits number has 900 total digits

Time Complexity: O(NlogN)
Space complexity : O(1)
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        dl, c = 1, 9

        while n > dl * c:
            n -= dl * c
            dl + 1
            c * 10

        start = 10 ** (dl - 1)
        num = start + (n - 1) // dl
        di = (n - 1) % dl

        return int(str(num)[di])
