"""
Solution 1:

Binary Search + Sliding Window

Time Complexity: O(NLogN)
Space complexity : O(1)
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        if not answerKey:
            return 0

        start, end = 1, len(answerKey)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.canWork(answerKey, k, mid):
                start = mid
            else:
                end = mid

        if self.canWork(answerKey, k, end):
            return end

        return start

    def canWork(self, answerKey, k, target):
        seenT = 0
        seenF = 0
        l = 0
        for r in range(len(answerKey)):
            if answerKey[r] == "T":
                seenT += 1
            if answerKey[r] == "F":
                seenF += 1

            while r - l > target - 1:
                if answerKey[l] == "T":
                    seenT -= 1
                if answerKey[l] == "F":
                    seenF -= 1
                l += 1

            if r - l >= target - 1 and (seenT <= k or seenF <= k):
                return True

        return False


"""
Solution 2:

Sliding Window

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        if not answerKey:
            return 0

        l, r = 0, 0
        seenT, seenF = 0, 0
        res = 0
        while r < len(answerKey):
            if answerKey[r] == "T":
                seenT += 1
            if answerKey[r] == "F":
                seenF += 1
            r += 1

            while l < r and seenT > k and seenF > k:
                if answerKey[l] == "T":
                    seenT -= 1
                if answerKey[l] == "F":
                    seenF -= 1
                l += 1

            res = max(res, r - l)

        return res
