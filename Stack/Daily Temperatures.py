"""
Solution 1:

Maintain a non-decreasing stack track the maximum temperature and it's index

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []

        stack = []
        res = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                res.append(stack[-1][1] - i)
            else:
                res.append(0)
            stack.append((temperatures[i], i))

        return res[::-1]
