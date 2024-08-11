"""
Solution 1:

Greedy

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []

        lastIdx = defaultdict(list)
        for i in range(len(s)):
            lastIdx[s[i]].append(i)

        res = []
        i = 0
        lastIndex = lastIdx[s[i]][-1]
        prev = 0
        while i < len(s):
            while i < lastIndex:
                i += 1
                lastIndex = max(lastIndex, lastIdx[s[i]][-1])

            res.append(lastIndex - prev + 1)
            prev = lastIndex + 1
            i += 1
            if i == len(s):
                break
            lastIndex = lastIdx[s[i]][-1]

        return res
