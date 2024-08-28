"""
Solution 1:

Set

Count ugly number one by one
If a number is ugly, multiplying it by 2, 3, or 5 also yields an ugly number

Time Complexity: O(n^2)
Space complexity : O(m)
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNumbers = set([1])
        res = 1
        for _ in range(n):
            res = min(uglyNumbers)

            uglyNumbers.remove(res)
            uglyNumbers.add(res * 2)
            uglyNumbers.add(res * 3)
            uglyNumbers.add(res * 5)

        return res


"""
Solution 2:

3 pointers

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNumbers = [0] * (n + 1)

        p, p2, p3, p5 = 1, 1, 1, 1
        product2, product3, product5 = 1, 1, 1

        for i in range(n):
            minValue = min(product2, product3, product5)
            uglyNumbers[p] = minValue
            p += 1

            if minValue == product2:
                product2 = 2 * uglyNumbers[p2]
                p2 += 1
            if minValue == product3:
                product3 = 3 * uglyNumbers[p3]
                p3 += 1
            if minValue == product5:
                product5 = 5 * uglyNumbers[p5]
                p5 += 1

        return minValue
