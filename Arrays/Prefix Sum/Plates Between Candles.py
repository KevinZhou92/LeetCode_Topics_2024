"""
Solution 1:

Brute Force

Time Complexity: O(n^2)
Space complexity : O(1)
"""


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        if not queries:
            return []

        res = []
        for q in queries:
            res.append(self.search(s, q))

        return res

    def search(self, s, q):
        p1Found = False
        cnt = 0
        tmp = 0
        for i in range(q[0], q[1] + 1):
            c = s[i]
            if c == "|":
                if not p1Found:
                    p1Found = True
                else:
                    cnt += tmp
                    tmp = 0
            else:
                if p1Found:
                    tmp += 1

        return cnt


"""
Solution 2:

Binary Search

Time Complexity: O(nlogn)
Space complexity : O(1)
"""


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        if not queries:
            return []

        res = []
        candleSums = [0 for _ in range(len(s))]
        candlePos = []
        for i in range(len(s)):
            candleSums[i] = candleSums[i - 1]
            if s[i] == "*":
                candleSums[i] += 1
            if s[i] == "|":
                candlePos.append(i)

        for q in queries:
            l = self.searchGreater(candlePos, q[0])
            r = self.searchSmaller(candlePos, q[1])
            print(l, r)
            if l == -1 or r == -1 or l >= r:
                res.append(0)
                continue
            res.append(candleSums[r] - candleSums[l])

        return res

    def searchGreater(self, array, target):
        if not array:
            return -1

        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if array[mid] > target:
                end = mid
            else:
                start = mid

        if array[start] >= target:
            return array[start]

        if array[end] < target:
            return -1

        return array[end]

    def searchSmaller(self, array, target):
        if not array:
            return -1

        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if array[mid] < target:
                start = mid
            else:
                end = mid

        if array[end] <= target:
            return array[end]

        if array[start] > target:
            return -1

        return array[start]


"""
Solution 3:

Tow Pointers

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        if not queries:
            return []

        res = []

        leftPos = [0] * len(s)
        rightPos = [0] * len(s)
        prefixSum = [0] * len(s)

        for i in range(len(s)):
            if i > 0:
                prefixSum[i] = prefixSum[i - 1]
            if s[i] == "*":
                prefixSum[i] += 1

        pos = -1
        for i in range(len(s)):
            if s[i] == "|":
                pos = i
            leftPos[i] = pos

        pos = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "|":
                pos = i
            rightPos[i] = pos

        for q in queries:
            l = rightPos[q[0]]
            r = leftPos[q[1]]
            if l < q[0] or r > q[1] or l >= r:
                res.append(0)
                continue
            res.append(prefixSum[r] - prefixSum[l])

        return res
