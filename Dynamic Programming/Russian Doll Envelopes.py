"""
Solution 1:

Dynamic Programming Problem, similar to Longest increasing sequence.

Trick #1: sort by first dimension(width), so we only need to care about comparing using height
Trick #2: sort second dimension in reverse order, so if we have envelope with same height, we don't mistakenly
count them in results due to the natural order of second dimension
Trick #3: Binary search to find the insertion point to reduce time complexity

Time Complexity: O(NlogN)
Space complexity : O(N)
"""

from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        envelopes = [e[1] for e in envelopes]
        dp = []
        for i in range(len(envelopes)):
            idx = bisect_left(dp, envelopes[i])
            if idx == len(dp):
                dp.append(envelopes[i])
            else:
                dp[idx] = envelopes[i]

        return len(dp)
